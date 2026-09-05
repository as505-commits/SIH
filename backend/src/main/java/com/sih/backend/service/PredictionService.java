package com.sih.backend.service;
import com.sih.backend.model.PredictionRequest;
import com.sih.backend.model.PredictionResponse;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PredictionService {
    private final RecommendationService recommendationService;
    private final AlertService alertService;
    private final RiskFactorService riskFactorService;
    public PredictionService(
            RecommendationService recommendationService,
            AlertService alertService,
            RiskFactorService riskFactorService) {
        this.recommendationService = recommendationService;
        this.alertService = alertService;
        this.riskFactorService = riskFactorService;
    }

    public PredictionResponse analyze(PredictionRequest request) {
        String stressLevel = "Pending";
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
}
