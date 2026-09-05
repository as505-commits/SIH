package com.sih.backend.service;

import com.sih.backend.model.PredictionRequest;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class RiskFactorService {

    public List<String> getRiskFactors(PredictionRequest request) {

        List<String> riskFactors = new ArrayList<>();

        // Low sleep
        if (request.getSleepHours() < 6) {
            riskFactors.add("Low sleep hours");
        }

        // High work pressure
        if (request.getWorkPressureLevel() != null &&
                request.getWorkPressureLevel().equalsIgnoreCase("High")) {

            riskFactors.add("High work pressure");
        }

        // Poor work-life balance
        if (request.getWorkLifeBalance() != null &&
                request.getWorkLifeBalance().equalsIgnoreCase("Low")) {

            riskFactors.add("Poor work-life balance");
        }

        // No training opportunities
        if (request.getTrainingOpportunities() != null &&
                request.getTrainingOpportunities().equalsIgnoreCase("No")) {

            riskFactors.add("Limited training opportunities");
        }

        // Long consecutive duty period
        if (request.getConsecutiveDutyDays() >= 7) {
            riskFactors.add("Long consecutive duty period");
        }

        // Too many days without leave
        if (request.getDaysSinceLastLeave() >= 30) {
            riskFactors.add("Long period since last leave");
        }

        // High deployment duration
        if (request.getDeploymentDays() >= 90) {
            riskFactors.add("High deployment duration");
        }

        // Frequent night shifts
        if (request.getNightShifts() >= 10) {
            riskFactors.add("Frequent night shifts");
        }

        return riskFactors;
    }
}
