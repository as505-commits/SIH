package com.sih.backend.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BackendController {

    @GetMapping("/api/status")
    public String status() {
        return "Backend is running successfully.";
    }
}