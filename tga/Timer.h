#ifndef TIMER_H
#define TIMER_H

#include <chrono>
#include <thread>
#include <ctime>

class Timer {

public:
    Timer();

    void start();
    void finish();

    double getElapsedTimeMs();
    double getElapsedTime();
    double calcWaitingTime(int fps, double elapsedTime);

protected:
    // Using time point and system_clock
    std::chrono::time_point<std::chrono::system_clock> begin, end;

};

#endif /* TIMER_H */
