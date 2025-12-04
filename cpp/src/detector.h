#pragma once
#include "csv_reader.h"
#include "rules.h"
#include <vector>
#include <map>

struct DetectionResult {
    Txn txn;
    RuleResult rules;
    bool stat_anomaly;
    int severity; // 0..3
    std::string why;
};

std::vector<DetectionResult> run_detection(const std::vector<Txn> &txns);

