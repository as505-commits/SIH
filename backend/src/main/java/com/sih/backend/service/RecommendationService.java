package com.sih.backend.service;

import org.springframework.stereotype.Service;

@Service
public class RecommendationService {

    public String getRecommendation(String stressLevel) {

        if (stressLevel == null) {
            return "No recommendation available.";
        }

        switch (stressLevel.toLowerCase()) {

            case "low":
                return "Maintain current workload and continue regular wellness activities.";

            case "medium":
                return "Consider workload balancing, adequate recovery time, and wellness support.";
                
            case "high":
                return "Recommend welfare officer intervention, workload review, and counseling support.";
                
            default:
                return "Stress level requires further assessment.";
        }
    }
}