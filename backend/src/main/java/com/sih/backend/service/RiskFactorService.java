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

        if (request.getWorkPressureLevel() >= 7) {
            riskFactors.add("High work pressure");
        }

        if (request.getConsecutiveDutyDays() >= 7) {
            riskFactors.add("Long consecutive duty period");
        }

        if (request.getDaysSinceLastLeave() >= 60) {
            riskFactors.add("Long time since last leave");
        }

        if (request.getWorkloadTrend() != null &&
                request.getWorkloadTrend().equalsIgnoreCase("Increasing")) {
            riskFactors.add("Increasing workload trend");
        }

        if (request.getWorkingHoursPerWeek() > 60) {
            riskFactors.add("High weekly working hours");
        }

        if (request.getNightShifts() >= 5) {
            riskFactors.add("Frequent night shifts");
        }

        return riskFactors;
    }
}
