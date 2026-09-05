package com.sih.backend.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import jakarta.validation.constraints.PositiveOrZero;

public class PredictionRequest {

    @JsonProperty("personnel_id")
    private String personnelId;

    @JsonProperty("Age")
    @PositiveOrZero
    private int age;

    @JsonProperty("Experience_Years")
    @PositiveOrZero
    private int experienceYears;

    @JsonProperty("Working_Hours_per_Week")
    @PositiveOrZero
    private double workingHoursPerWeek;

    @JsonProperty("Sleep_Hours")
    @PositiveOrZero
    private double sleepHours;

    @JsonProperty("Physical_Activity_Hours_per_Week")
    @PositiveOrZero
    private double physicalActivityHoursPerWeek;

    @JsonProperty("Work_Pressure_Level")
    private String workPressureLevel;

    @JsonProperty("Annual_Leaves_Taken")
    @PositiveOrZero
    private int annualLeavesTaken;

    @JsonProperty("Work_Life_Balance")
    private String workLifeBalance;

    @JsonProperty("Family_Support_Level")
    private String familySupportLevel;

    @JsonProperty("Job_Satisfaction")
    private String jobSatisfaction;

    @JsonProperty("Training_Opportunities")
    private String trainingOpportunities;

    @JsonProperty("Deployment_Days")
    @PositiveOrZero
    private int deploymentDays;

    @JsonProperty("Night_Shifts")
    @PositiveOrZero
    private int nightShifts;

    @JsonProperty("Consecutive_Duty_Days")
    @PositiveOrZero
    private int consecutiveDutyDays;

    @JsonProperty("Days_Since_Last_Leave")
    @PositiveOrZero
    private int daysSinceLastLeave;

    @JsonProperty("Transfer_Count")
    @PositiveOrZero
    private int transferCount;

    @JsonProperty("Recovery_Days")
    @PositiveOrZero
    private int recoveryDays;

    @JsonProperty("Duty_Hours_Avg")
    @PositiveOrZero
    private double dutyHoursAvg;

    @JsonProperty("Workload_Trend")
    private double workloadTrend;

    public PredictionRequest() {
    }

    public String getPersonnelId() {
        return personnelId;
    }

    public void setPersonnelId(String personnelId) {
        this.personnelId = personnelId;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getExperienceYears() {
        return experienceYears;
    }

    public void setExperienceYears(int experienceYears) {
        this.experienceYears = experienceYears;
    }

    public double getWorkingHoursPerWeek() {
        return workingHoursPerWeek;
    }

    public void setWorkingHoursPerWeek(double workingHoursPerWeek) {
        this.workingHoursPerWeek = workingHoursPerWeek;
    }

    public double getSleepHours() {
        return sleepHours;
    }

    public void setSleepHours(double sleepHours) {
        this.sleepHours = sleepHours;
    }

    public double getPhysicalActivityHoursPerWeek() {
        return physicalActivityHoursPerWeek;
    }

    public void setPhysicalActivityHoursPerWeek(double physicalActivityHoursPerWeek) {
        this.physicalActivityHoursPerWeek = physicalActivityHoursPerWeek;
    }

    public String getWorkPressureLevel() {
        return workPressureLevel;
    }

    public void setWorkPressureLevel(String workPressureLevel) {
        this.workPressureLevel = workPressureLevel;
    }

    public int getAnnualLeavesTaken() {
        return annualLeavesTaken;
    }

    public void setAnnualLeavesTaken(int annualLeavesTaken) {
        this.annualLeavesTaken = annualLeavesTaken;
    }

    public String getWorkLifeBalance() {
        return workLifeBalance;
    }

    public void setWorkLifeBalance(String workLifeBalance) {
        this.workLifeBalance = workLifeBalance;
    }

    public String getFamilySupportLevel() {
        return familySupportLevel;
    }

    public void setFamilySupportLevel(String familySupportLevel) {
        this.familySupportLevel = familySupportLevel;
    }

    public String getJobSatisfaction() {
        return jobSatisfaction;
    }

    public void setJobSatisfaction(String jobSatisfaction) {
        this.jobSatisfaction = jobSatisfaction;
    }

    public String getTrainingOpportunities() {
        return trainingOpportunities;
    }

    public void setTrainingOpportunities(String trainingOpportunities) {
        this.trainingOpportunities = trainingOpportunities;
    }

    public int getDeploymentDays() {
        return deploymentDays;
    }

    public void setDeploymentDays(int deploymentDays) {
        this.deploymentDays = deploymentDays;
    }

    public int getNightShifts() {
        return nightShifts;
    }

    public void setNightShifts(int nightShifts) {
        this.nightShifts = nightShifts;
    }

    public int getConsecutiveDutyDays() {
        return consecutiveDutyDays;
    }

    public void setConsecutiveDutyDays(int consecutiveDutyDays) {
        this.consecutiveDutyDays = consecutiveDutyDays;
    }

    public int getDaysSinceLastLeave() {
        return daysSinceLastLeave;
    }

    public void setDaysSinceLastLeave(int daysSinceLastLeave) {
        this.daysSinceLastLeave = daysSinceLastLeave;
    }

    public int getTransferCount() {
        return transferCount;
    }

    public void setTransferCount(int transferCount) {
        this.transferCount = transferCount;
    }

    public int getRecoveryDays() {
        return recoveryDays;
    }

    public void setRecoveryDays(int recoveryDays) {
        this.recoveryDays = recoveryDays;
    }

    public double getDutyHoursAvg() {
        return dutyHoursAvg;
    }

    public void setDutyHoursAvg(double dutyHoursAvg) {
        this.dutyHoursAvg = dutyHoursAvg;
    }

    public double getWorkloadTrend() {
        return workloadTrend;
    }

    public void setWorkloadTrend(double workloadTrend) {
        this.workloadTrend = workloadTrend;
    }
}
