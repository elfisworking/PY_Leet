#include<string>
#include<map>
#include<cmath>
using namespace std;
class Solution {
public:
    string getHint(string secret, string guess) {
        int sec[10] = {0};
        int gue[10] = {0};

        int bulls = 0;
        int cows = 0;
        for(int i = 0; i < secret.size(); i++) {
            if(secret[i] == guess[i]) {
                bulls ++;
            }else {
                sec[secret[i] - '0']++;
                gue[guess[i] - '0']++;
            }
        }

        for(int i =0; i < 10; i++) {
            cows += min(sec[i], gue[i]);
        }

        return to_string(bulls) + "A" + to_string(cows) + "B";
    }
};