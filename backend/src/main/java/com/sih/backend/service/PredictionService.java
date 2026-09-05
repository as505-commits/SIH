package com.sih.backend.service;

import com.sih.backend.model.PredictionRequest;
import com.sih.backend.model.PredictionResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestClient;

import java.util.List;

@Service
public class PredictionService {

    private final RecommendationService recommendationService;
    private final AlertService alertService;
    private final RiskFactorService riskFactorService;
    private final RestClient restClient;

    public PredictionService(
            RecommendationService recommendationService,
            AlertService alertService,
            RiskFactorService riskFactorService,
            @Value("${ml.api.url:http://localhost:8000}") String mlApiUrl) {

        this.recommendationService = recommendationService;
        this.alertService = alertService;
        this.riskFactorService = riskFactorService;
        this.restClient = RestClient.builder()
                .baseUrl(mlApiUrl)
                .build();
    }

    public PredictionResponse analyze(PredictionRequest request) {

        PythonPredictionResponse prediction =
                restClient.post()
                        .uri("/predict")
                        .body(request)
                        .retrieve()
                        .body(PythonPredictionResponse.class);

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
