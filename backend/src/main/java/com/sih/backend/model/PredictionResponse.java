package com.sih.backend.model;

import java.util.List;

public class PredictionResponse {

    private String stressLevel;
    private String recommendation;
    private String alert;
    private List<String> riskFactors;

    public PredictionResponse() {
    }

    public PredictionResponse(
            String stressLevel,
            String recommendation,
            String alert,
            List<String> riskFactors) {

        this.stressLevel = stressLevel;
        this.recommendation = recommendation;
        this.alert = alert;
        this.riskFactors = riskFactors;
    }

    public String getStressLevel() {
        return stressLevel;
    }

    public void setStressLevel(String stressLevel) {
        this.stressLevel = stressLevel;
    }

    public String getRecommendation() {
        return recommendation;
    }

    public void setRecommendation(String recommendation) {
        this.recommendation = recommendation;
    }

    public String getAlert() {
        return alert;
    }

    public void setAlert(String alert) {
        this.alert = alert;
    }

    public List<String> getRiskFactors() {
        return riskFactors;
    }

    public void setRiskFactors(List<String> riskFactors) {
        this.riskFactors = riskFactors;
    }
}