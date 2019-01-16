//（1） 大数的加减乘除运算
//参考链接https://www.cnblogs.com/FZfangzheng/p/7700699.html

// 乘法

#include<iostream>
#include<string>
using namespace std;
int main()
{
    string str1,str2;
    int lena,lenb,num;
    int a[100],b[100];
    int sum[200]={0};      // 数组初始化为0
    cin>>str1>>str2;
    
    lena = str1.length();    // 计算字符串长度
    lenb = str2.length();
    
    // 数字字符转化为整数
     for(int i=0;i<lena;i++){
         a[i] = str1[i]-48;
     }
     for(int j=0;j<lenb;j++){
         b[j] = str2[j]-48;
     }
     
    //核心部分
    for(int i=lenb-1;i>=0;i--){
        num = lenb-1-i;
        for(int j=lena-1;j>=0;j--){
            sum[num++] += b[i]*a[j];
        }
    }
    
    // 调整进位
    for(int i=0;i<num;i++){
        if(sum[num-1]>=10){
            num++;
        }
        sum[i+1] += sum[i]/10;
        sum[i] = sum[i]%10;
    }
    
    //输出
    for (int i=num-1;i>=0;i--){
        cout<<sum[i];
    }
    return 0;
}
