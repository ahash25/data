Activity Selection:
#include <bits/stdc++.h> 
using namespace std; 
struct Activity { 
int start, end; 
}; 
bool compare(Activity a, Activity b) { 
return (a.end < b.end); 
} 
void printMaxActivities(Activity arr[], int n) { 
sort(arr, arr + n, compare); 
cout << "Following activities are selected: \n"; 
int i = 0; 
cout << "(" << arr[i].start << ", " << arr[i].end << "), "; 
for (int j = 1; j < n; j++) { 
if (arr[j].start >= arr[i].end) { 
cout << "(" << arr[j].start << ", " << arr[j].end << "), "; 
i = j; 
} 
} 
} 
int main() { 
Activity arr[] = {{5, 9}, {1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}}; 
int n = sizeof(arr) / sizeof(arr[0]); 
printMaxActivities(arr, n);
return 0;
}
