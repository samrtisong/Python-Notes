// (1) 字符串处理----删除重复的字符
#include<iostream>
#include<string>
using namespace std;
int main()
{
   string str,ss;
   cin >> str;

   for(int i=0;i<str.length();i++){
	   //cout << str.find(str[i]) << ',';
	   if (ss.find(str[i]) == string::npos){
		   ss+=str[i];
       }
   }
	cout << ss << endl;
   return 0;
}





// (2)数组处理




