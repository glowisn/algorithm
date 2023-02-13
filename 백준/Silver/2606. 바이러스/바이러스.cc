#include <iostream>
#include <stack>
#include <vector>

using std::cin; using std::cout; using std::endl;

std::stack<int> stack;
std::vector<int> nodes[101];
bool visited[101] = {false,};
int count = 0;

void deep(int top);

int main(){
    int dotn, linen;
    cin >> dotn >> linen;

    for(int i = 1; i <= linen; i++){
        int a,b;
        cin >> a >> b;
        nodes[a].push_back(b);
        nodes[b].push_back(a);
    }

    deep(1);

    cout << count;
    
}

void deep(int top){
    stack.push(top);
    visited[top] = true;
    for(int i = 0; i < nodes[top].size();i++){
        if(!visited[nodes[top][i]]){
            count++;
            deep(nodes[top][i]);
        }
    }
    stack.pop();
}