class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        for (string s : tokens) {
            if (s == "+") {
                auto [operand1, operand2] = getOperands(stk);
                stk.push(operand1 + operand2);
            }
            if (s == "-") {
                auto [operand1, operand2] = getOperands(stk);
                stk.push(operand1 - operand2);
            }
            if (s == "*") {
                auto [operand1, operand2] = getOperands(stk);
                stk.push(operand1 * operand2);
            }
            if (s == "/") {
                auto [operand1, operand2] = getOperands(stk);
                stk.push(int(operand1 / operand2));
            }
            if (s != "+" && s != "-" && s != "*" && s != "/") {
                stk.push(stoi(s));
            }
        }
        
        return stk.top();
    }

private:
    pair<int, int> getOperands(stack<int>& stk) {
        int operand1, operand2; 
        operand2 = stk.top();
        stk.pop();
        operand1 = stk.top();
        stk.pop();
        return {operand1, operand2};
    }
};