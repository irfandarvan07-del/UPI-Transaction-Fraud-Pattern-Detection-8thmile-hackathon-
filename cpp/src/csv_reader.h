#pragma once
#include <string>
#include <vector>

struct Txn {
    std::string txn_id;
    std::string timestamp;
    std::string from_vpa;
    std::string to_vpa;
    double amount;
    std::string message;
    int is_new_payee;
};

std::vector<Txn> read_csv(const std::string &path);

