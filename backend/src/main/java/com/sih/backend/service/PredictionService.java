package com.sih.backend.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.sih.backend.model.PredictionRequest;
import com.sih.backend.model.PredictionResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.List;

@Service
public class PredictionService {

    private final RecommendationService recommendationService;
    private final AlertService alertService;
    private final RiskFactorService riskFactorService;
    private final ObjectMapper objectMapper = new ObjectMapper();
    private final HttpClient httpClient = HttpClient.newBuilder()
            .version(HttpClient.Version.HTTP_1_1)
            .build();
    private final String mlApiUrl;

    public PredictionService(
            RecommendationService recommendationService,
            AlertService alertService,
            RiskFactorService riskFactorService,
            @Value("${ml.api.url:http://localhost:8000}") String mlApiUrl) {

        this.recommendationService = recommendationService;
        this.alertService = alertService;
        this.riskFactorService = riskFactorService;
        this.mlApiUrl = mlApiUrl;
    }

    public PredictionResponse analyze(PredictionRequest request) {

        final String requestJson;

        try {
            requestJson = objectMapper.writeValueAsString(request);
        } catch (JsonProcessingException error) {
            throw new IllegalStateException(
                    "Could not convert the personnel request to JSON",
                    error
            );
        }
        final HttpRequest httpRequest = HttpRequest.newBuilder()
                .uri(URI.create(mlApiUrl + "/predict"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(
                        requestJson,
                        StandardCharsets.UTF_8
                ))
                .build();

        final HttpResponse<String> httpResponse;

        try {
            httpResponse = httpClient.send(
                    httpRequest,
                    HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8)
            );
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new IllegalStateException(
                    "The request to the Python API was interrupted",
                    error
            );
        } catch (Exception error) {
            throw new IllegalStateException(
                    "Could not connect to the Python API at " + mlApiUrl,
                    error
            );
        }

        if (httpResponse.statusCode() < 200 || httpResponse.statusCode() >= 300) {
            throw new IllegalStateException(
                    "Python API returned HTTP "
                            + httpResponse.statusCode()
                            + ": "
                            + httpResponse.body()
            );
        }

        final PythonPredictionResponse prediction;

        try {
            prediction = objectMapper.readValue(
                    httpResponse.body(),
                    PythonPredictionResponse.class
            );
        } catch (JsonProcessingException error) {
            throw new IllegalStateException(
                    "Python API returned invalid JSON: " + httpResponse.body(),
                    error
            );
        }

        if (prediction == null || prediction.risk() == null) {
            throw new IllegalStateException("Python API returned an empty prediction");
        }

        String stressLevel = prediction.risk();

        List<String> riskFactors =
                riskFactorService.getRiskFactors(request);

        String recommendation =
                recommendationService.getRecommendation(stressLevel);

        String alert =
                alertService.getAlert(stressLevel);

        return new PredictionResponse(
                stressLevel,
                recommendation,
                alert,
                riskFactors
        );
    }

    private record PythonPredictionResponse(
            String personnel_id,
            String risk,
            double confidence
    ) {
    }
}
