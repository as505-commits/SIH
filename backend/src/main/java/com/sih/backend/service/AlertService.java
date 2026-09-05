package com.sih.backend.service;

import org.springframework.stereotype.Service;

@Service
public class AlertService {

    public String getAlert(String stressLevel) {

        if (stressLevel == null) {
            return "No alert available.";
        }

        switch (stressLevel.toLowerCase()) {

            case "high":
                return "HIGH PRIORITY: Welfare officer attention recommended.";

            case "medium":
                return "MONITOR: Consider welfare support and workload review.";

            case "low":
                return "No immediate welfare alert.";

            default:
                return "Stress level pending assessment.";
        }
    }
}