package com.sih.backend.service;

import com.sih.backend.model.PredictionRequest;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

@Service
public class RiskFactorService {
    public List<String> getRiskFactors(PredictionRequest request) {
        List<String> riskFactors = new ArrayList<>();
        if (request.getSleepHours() < 6) {
            riskFactors.add("Low sleep hours");
        }

        if (request.getWorkPressureLevel() != null &&
                request.getWorkPressureLevel().equalsIgnoreCase("High")) {
            riskFactors.add("High work pressure");
        }

        if (request.getWorkLifeBalance() != null &&
                request.getWorkLifeBalance().equalsIgnoreCase("Low")) {
            riskFactors.add("Poor work-life balance");
        }

        if (request.getTrainingOpportunities() != null &&
                request.getTrainingOpportunities().equalsIgnoreCase("No")) {
            riskFactors.add("Limited training opportunities");
        }

        if (request.getConsecutiveDutyDays() >= 7) {
            riskFactors.add("Long consecutive duty period");
        }

        if (request.getDaysSinceLastLeave() >= 30) {
            riskFactors.add("Long period since last leave");
        }

        if (request.getDeploymentDays() >= 90) {
            riskFactors.add("High deployment duration");
        }

        if (request.getNightShifts() >= 10) {
            riskFactors.add("Frequent night shifts");
        }

        return riskFactors;
    }
}
