#include <iostream>
#include <string>
using namespace std;


string _subsequences(string s, string res){
    if(s.length()==0){
        // string res = res + ',';
        return res;
    }
    char firstchar = s[0];
    string s2="";
    for(int i=2;i<s.length();i++){
        s2 += s[i];
    }
    string res2 =_subsequences(s2,res);
    for(int i=0;i<res2.length();i++){
        string word = "";
        
        if (res2[i] == ','){
            res+= word;
            res+=',';
            res+= firstchar + word;
            res+=',';
        }else{
            word += res2[i];
        }
        
    }

    return res;
}

string subsequences(string s){
    string res = "";
    
    _subsequences(s,res);
    return res;
}

int main(){
    string s = "hello";
    string res = subsequences(s);
    cout<<res<<"\n";


}