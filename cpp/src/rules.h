#pragma once
#include "csv_reader.h"
#include <string>
#include <vector>

struct RuleResult {
    bool suspicious_msg = false;
    bool micro_cluster = false;
    bool high_amount = false;
    bool new_payee = false;
    std::vector<std::string> reasons;
};

RuleResult apply_rules(const Txn &t);
bool contains_keyword(const std::string &s);

