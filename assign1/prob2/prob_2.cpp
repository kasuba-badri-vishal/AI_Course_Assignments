#include<bits/stdc++.h>

using namespace std;

bool UP(int x1,int y1, vector<vector<bool>> grid) {
    if(x1<grid.size() && y1<grid[0].size()) {
        if(x1==0) return false;
        else if(grid[x1-1][y1]==true) return false;
        else return true;
    }
    else return false;
}

bool DOWN(int x1,int y1, vector<vector<bool>> grid) {
    if(x1<grid.size() && y1<grid[0].size()) {
        if(x1==grid.size()-1) return false;
        else if(grid[x1+1][y1]==true) return false;
        else return true;
    }
    else return false;
}

bool RIGHT(int x1,int y1, vector<vector<bool>> grid) {
    if(x1<grid.size() && y1<grid[0].size()) {
        if(y1==grid[0].size()-1) return false;
        else if(grid[x1][y1+1]==true) return false;
        else return true;
    }
    else return false;
}

bool LEFT(int x1,int y1, vector<vector<bool>> grid) {
    if(x1<grid.size() && y1<grid[0].size()) {
        if(y1==0) return false;
        else if(grid[x1][y1-1]==true) return false;
        else return true;
    }
    else return false;
}

void DFS(int x1,int y1,int x2,int y2,vector<vector<bool>> grid,stack<pair<int,int>> s,int c) {
    if(x1==x2 && y1==y2) {
        cout << "(" << x1 << "," << y1 << ",X)\n";
        cout << "Above is the direction found using DFS backtracking\n";
        return;
    }
    else {
        cout << "(" << x1 << "," << y1 << ",";
        grid[x1][y1] = true;
        if(DOWN(x1,y1,grid)) { cout <<"D)->"; s.push(make_pair(x1,y1)); c=1;DFS(x1+1,y1,x2,y2,grid,s,c); }
        else if(RIGHT(x1,y1,grid)) { cout <<"R)->"; c=3;s.push(make_pair(x1,y1)); DFS(x1,y1+1,x2,y2,grid,s,c); }
        else if(UP(x1,y1,grid)) { cout <<"U)->"; c=2; s.push(make_pair(x1,y1)); DFS(x1-1,y1,x2,y2,grid,s,c); }
        else if(LEFT(x1,y1,grid)) { cout <<"L)->"; c=4; s.push(make_pair(x1,y1));DFS(x1,y1-1,x2,y2,grid,s,c); }
        else {
                pair<int,int> temp = s.top();
                s.pop();
                pair<int,int> temp2 = s.top(); 
                if(c==1)  cout <<"U)->"; 
                else if(c==2) cout <<"D)->";
                else if(c==3) cout <<"L)->";
                else cout <<"R)->";
                if(temp.first==temp2.first && temp.second<temp2.second) c=4;
                else if(temp.first==temp2.first && temp.second>temp2.second) c=3;
                else if(temp.first<temp2.first && temp.second==temp2.second) c=2;
                else c=1;
                DFS(temp.first,temp.second,x2,y2,grid,s,c);
                
            }
    }
    return;
}

int main() {

    int n,m;
    cout << "Enter the dimensions of grid : ";
    cin >> n >> m;
    vector< vector<bool> > grid(n,vector<bool>(m,false));
    cout << "Number of Obstacles : ";
    int obs;
    cin >> obs;
    cout << "Enter the Obstacle location\n";
    int x,y;
    for(int i=0;i<obs;i++) {
        cin >> x >> y;
        grid[x][y] = true;
    }
    int start_x,start_y,end_x,end_y;
    cout << "Enter the Start location : ";
    cin >> start_x >> start_y;
    cout << "Enter the End location : ";
    cin >> end_x >> end_y;
    for(int i=0;i<n;i++) {
        for(int j=0;j<m;j++) {
            cout << grid[i][j] << " ";
        }
        cout << "\n";
    }
    stack <pair<int,int> > s;
    int c = 1;
    DFS(start_x,start_y,end_x,end_y,grid,s,c);
    return 0;
}