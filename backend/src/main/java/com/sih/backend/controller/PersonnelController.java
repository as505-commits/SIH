package com.sih.backend.controller;
import com.sih.backend.model.PredictionRequest;
import com.sih.backend.model.PredictionResponse;
import com.sih.backend.service.PredictionService;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/api/personnel")
@CrossOrigin(origins = "*")
public class PersonnelController {
    private final PredictionService predictionService;
    public PersonnelController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }
    @GetMapping("/test")
    public String test() {
        return "Personnel backend is working!";
    }
    @PostMapping("/analyze")
    public PredictionResponse analyze(@RequestBody PredictionRequest request) {
        return predictionService.analyze(request);
    }
}
