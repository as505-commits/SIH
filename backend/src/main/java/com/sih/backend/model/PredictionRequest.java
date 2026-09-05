package com.sih.backend.model;
import jakarta.validation.constraints.PositiveOrZero;
public class PredictionRequest {

    @PositiveOrZero
    private int age;
    @PositiveOrZero
    private int experienceYears;
    @PositiveOrZero
    private double workingHoursPerWeek;
    @PositiveOrZero
    private double sleepHours;
    @PositiveOrZero
    private double physicalActivityHoursPerWeek;
    @PositiveOrZero
    private int workPressureLevel;
    @PositiveOrZero
    private int annualLeavesTaken;
    @PositiveOrZero
    private int workLifeBalance;
    @PositiveOrZero
    private int familySupportLevel;
    @PositiveOrZero
    private int jobSatisfaction;
    @PositiveOrZero
    private int trainingOpportunities;
    @PositiveOrZero
    private int deploymentDays;
    @PositiveOrZero
    private int nightShifts;
    @PositiveOrZero
    private int consecutiveDutyDays;
    @PositiveOrZero
    private int daysSinceLastLeave;
    @PositiveOrZero
    private int transferCount;
    @PositiveOrZero
    private int recoveryDays;
    @PositiveOrZero
    private double dutyHoursAvg;
    private String workloadTrend;
    public PredictionRequest() {
    }

    // Getters and setters

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

    public int getWorkPressureLevel() {
        return workPressureLevel;
    }

    public void setWorkPressureLevel(int workPressureLevel) {
        this.workPressureLevel = workPressureLevel;
    }

    public int getAnnualLeavesTaken() {
        return annualLeavesTaken;
    }

    public void setAnnualLeavesTaken(int annualLeavesTaken) {
        this.annualLeavesTaken = annualLeavesTaken;
    }

    public int getWorkLifeBalance() {
        return workLifeBalance;
    }

    public void setWorkLifeBalance(int workLifeBalance) {
        this.workLifeBalance = workLifeBalance;
    }

    public int getFamilySupportLevel() {
        return familySupportLevel;
    }

    public void setFamilySupportLevel(int familySupportLevel) {
        this.familySupportLevel = familySupportLevel;
    }

    public int getJobSatisfaction() {
        return jobSatisfaction;
    }

    public void setJobSatisfaction(int jobSatisfaction) {
        this.jobSatisfaction = jobSatisfaction;
    }

    public int getTrainingOpportunities() {
        return trainingOpportunities;
    }

    public void setTrainingOpportunities(int trainingOpportunities) {
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

    public String getWorkloadTrend() {
        return workloadTrend;
    }

    public void setWorkloadTrend(String workloadTrend) {
        this.workloadTrend = workloadTrend;
    }
}