
# 파이썬 코드를 c++로 옮기니까 통과된다. 부들부들

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
const int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};
const int r_ = 2000, rc_ = 4000001;
char pacific[r_][r_];
int n, m, order, num, vis[r_][r_], discovered[rc_], con[rc_], isIsland[rc_], ap[rc_];
vector<int> stack, queue, adj[rc_];
void dfs(int y, int x, int num) {
  vis[y][x] = num;
  for (int i = 0; i < 4; i++) {
      int yi = y + dy[i], xi = x + dx[i];
      if (0 <= yi && yi < n && 0 <= xi && xi < m) {
          if (pacific[y][x] == pacific[yi][xi] && !vis[yi][xi]) {
              dfs(yi, xi, num);
          }
          else if (pacific[y][x] != pacific[yi][xi] && vis[yi][xi]) {
              if (con[vis[yi][xi]] == num) continue;
              adj[num].push_back(vis[yi][xi]);
              adj[vis[yi][xi]].push_back(num);
              con[num] = num;
              con[vis[yi][xi]] = num;
          }
      }
  }
}
int findCutVertex(int now) {
  discovered[now] = ++order;
  stack.push_back(now);
  int ret = discovered[now];
  for (int nxt : adj[now]) {
      if (!discovered[nxt]) {
          int subtree = findCutVertex(nxt);
          if (isIsland[now] && subtree >= discovered[now]) {
              ap[now] = 1;
              while (!stack.empty() && stack.back() != now) {
                  con[stack.back()] = 1;
                  stack.pop_back();
              }
          }
          stack.push_back(now);
          ret = min(ret, subtree);
      }
      else {
          ret = min(ret, discovered[nxt]);
      }
  }
  return ret;
}
void input() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) scanf("%s", pacific[i]);
  stack.reserve(rc_);
}
void process() {
  for (int j = 0; j < n; j++) {
      for (int i = 0; i < m; i++) {
      if (!vis[j][i]) dfs(j, i, ++num);
      if (pacific[j][i] == '#') isIsland[vis[j][i]] = 1;
      }
  }
  fill(con, con+num+1, 0);
  findCutVertex(1);
}
void output() {
  for (int j = 0; j < n; j++) {
      for (int i = 0; i < m; i++) {
          if (pacific[j][i] == '.') {
              printf(".");
              continue;
          }
          int num = vis[j][i];
          printf("%c", con[num] && discovered[num] != 1 ? 'X' : 'O');
      }
      puts("");
  }
}

int main() {
  input();
  process();
  output();
  return 0;
}