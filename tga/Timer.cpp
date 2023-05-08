#include <chrono>
#include <thread>
#include <ctime>
#include "Timer.h"

Timer::Timer() {}

void Timer::start() {
    begin = std::chrono::system_clock::now();
}

void Timer::finish() {
    end = std::chrono::system_clock::now();
}

double Timer::getElapsedTimeMs() {
    std::chrono::duration<double> elapsed_seconds = end - begin;
    return elapsed_seconds.count() * 1000;
}

double Timer::getElapsedTime() {
    std::chrono::duration<double> elapsed_seconds = end - begin;
    return elapsed_seconds.count();
}

double Timer::calcWaitingTime(int fps, double elapsedTime) {
    double wt = 1000 / (double)fps - elapsedTime;
    return wt;
}
