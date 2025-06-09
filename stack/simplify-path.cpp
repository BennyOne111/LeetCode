class Solution {
public:
    string simplifyPath(string path) {
        string simplifiedCanonicalPath = "";
        stack<string> pathStack;
        string currentDir = "";
        for (int i = 1; i < path.size(); i++) {
            if ((path[i] == '/') || (i == path.size() - 1)) {
                if ((i == path.size() - 1) && (path[i] != '/')) currentDir += path[i];
                if (currentDir != "") {
                    if (currentDir == ".") {
                        currentDir = "";
                        continue;
                    }                            
                    if (currentDir == "..") { if (!pathStack.empty()) pathStack.pop(); }
                    if (currentDir != "." && currentDir != "..") pathStack.push(currentDir);
                    currentDir = "";
                }
            }
            else currentDir += path[i];
        }
        
        while (!pathStack.empty()) {
            simplifiedCanonicalPath = "/" + pathStack.top() + simplifiedCanonicalPath;
            pathStack.pop();
        }
        if (simplifiedCanonicalPath == "") simplifiedCanonicalPath = "/";

        return simplifiedCanonicalPath;
    }
};