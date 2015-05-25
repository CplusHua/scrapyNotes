#include <iostream>
  #include <fstream>
  
  #include "NTL/ZZ.h"
  #include "NTL/ZZ_p.h"
  #include "NTL/ZZX.h"
  #include "NTL/ZZ_pX.h"
  #include "NTL/ZZ_pXFactoring.h"
  
  #include "md5.h"
  
  #undef  F(x,y,z)
  #define F(x, y, z) (((x)&((y)^(z)))^(z))
  
  #undef  G(x,y,z)
  #define G(x, y, z) ((((x)^(y))&(z))^(y))
  
  using namespace NTL;
  using namespace std;
  
  void encode(unsigned char *input,unsigned char *output,unsigned int length,unsigned int value){
    unsigned int keysize=length*3*0x14;
    unsigned int *key=(unsigned int *)malloc(keysize*4);
    memset(key,0,keysize*4);
    memcpy(output,input,length);
    unsigned int shiftlength;
    unsigned __int64 pos;
    if(value==0x20A48C)
      //bug?
      key[0]=0xDB7427AC+1;
    else
      key[0]=value*0x8088405+1;
    for(unsigned int i=1;i<keysize;i++)
      key[i]=0x8088405*key[i-1]+1;
  
    for( unsigned int i=0;i<0x14;i++){
      for(unsigned int j=0;j<length;j++){
        output[length-1-j]^=key[keysize-1-2*j-i*3*length]>>24;
        shiftlength=key[keysize-2-2*j-i*3*length]>>29;
        output[length-1-j]=output[length-1-j]<<shiftlength|output[length-1-j]>>(8-shiftlength);
  
      }
      for(unsigned int j=0;j<length;j++){
        pos=key[keysize-2*length-1-j-i*3*length];
        pos=(pos*length)>>32;
        unsigned char temp=output[length-1-j];
        output[length-1-j]=output[pos];
        output[pos]=temp;
  
      }
    }
    if(key!=NULL){
      free(key);
      key=NULL;
    }
  }
  
  void MD5CustomFinal (unsigned char digest[16],MD5_CTX *context)
  {
    unsigned char bits[8];
    unsigned int index, padLen,i;
    unsigned char extra[0x40];
    //custom
    for(i=0;i<0x40;i++)
       extra[i]=3*i;
    Encode (bits, context->count, 8);
    index = (unsigned int)((context->count[0] >> 3) & 0x3f);
    padLen = (index < 56) ? (56 - index) : (120 - index);
    MD5Update (context, PADDING, padLen);
    MD5Update (context, bits, 8);
    //custom
    MD5Update(context,extra,0x40);
    Encode (digest, context->state, 16);
    MD5_memset ((POINTER)context, 0, sizeof (*context));
  }
  
  ZZX GenPoly(const ZZ &p,const ZZ &e){
    ZZ_p::init(p);
    long len=NumBits(e);
    ZZ_pX constpoly(0,2);
    ZZ_pX poly(1,1);
    ZZ_pX final=constpoly;
    ZZ_pX temp=poly;
    for(long i=len-1;i>=0;i--){
      if(bit(e,i)==1){
        
        final=final*temp-poly;
        temp=temp*temp-constpoly;
      }else
      {
        temp=temp*final-poly;
        final=final*final-constpoly;
      }
    }
      return to_ZZX(final);
  }
  
  void BuildPolysForRoots(const vec_ZZ &primes,const ZZ &e,vec_ZZX &polys){
    int len=primes.length();
    for(int i=0;i<len;i++)
      append(polys,GenPoly(primes[i],e));
  }
  
  ZZ CRTS(vec_ZZ primes,vec_ZZ rems){
    int len=primes.length();
    for(int i=0;i<len-1;i++){
      CRT(rems[i+1],primes[i+1],rems[i],primes[i]);
      
;rems[i+1]%=primes[i+1];
    }
    return rems[len-1];
   }
  
  ZZ BruteForce(const vec_ZZ &primes,const vec_ZZX &polys,const ZZ &M){
    int len=primes.length();
    vec_ZZ roots;
    roots.SetLength(len);
    for(int i=0;i<len;i++){
      ZZ_p::init(primes[i]);
      ZZ_pX rootpoly=to_ZZ_pX(polys[i]);
      SetCoeff(rootpoly,0,-to_ZZ_p(M));
      roots[i]=rep(FindRoot(rootpoly));
    }
      return CRTS(primes,roots);
    
  }
  
  ZZ Encrypt(const vec_ZZ &primes,const ZZ &e,const ZZ &M){
     vec_ZZX polys;
     BuildPolysForRoots(primes,e,polys);
     return BruteForce(primes,polys,M);
  }
  
  ZZ GenPrimes(vec_ZZ &primes,const ZZ &initvalue,const long &count){
    ZZ modulus=to_ZZ(1);
    ZZ prime=initvalue;
    for(int i=0;i<count;i++){
      prime=NextPrime(prime+1);
      append(primes,prime);
      modulus*=prime;
    }
    return modulus;
  }
  
  void GenReg(){
    ofstream out("wincmd.key",ios::binary);
    char reginfo[0x50]="CHNpediy|pediy|pediy";
    unsigned int regno=0xFFFFFE;
    unsigned short number=0xFFFE;
    unsigned char reg[0x400];
    memset(reg,0,0x400);
    MD5_CTX context;
    MD5Init(&context);
    MD5Update(&context,reg+0x380,0x70);
    MD5CustomFinal(reg+0x3F0,&context);
    encode(reg+0x3F0,reg+0x3F0,0x10,0x8800);
    *(reg+0x90)=regno>>0x10;
    memcpy(reg+0x91,&regno,2);
    memcpy(reg+0x93,&number,2);
    memcpy(reg+0x97,reginfo,strlen(reginfo));
    MD5Init(&context);
    MD5Update(&context,reg+0x90,0x57);
    MD5CustomFinal(reg+0x80,&context);
    encode(reg+0x80,reg+0x80,0x67,0x20A48C);
    vec_ZZ primes;
    ZZ modulus=GenPrimes(primes,to_ZZ(0x1E00),64);
    cout<<"modulus:"<<endl;
    cout<<modulus<<endl;
    ZZ e=to_ZZ("65537");
    cout<<"e:"<<e<<endl;
    ZZ M=ZZFromBytes(reg+0x80,0x68);
    ZZ C=Encrypt(primes,e,M);
    BytesFromZZ(reg+0x80,C,0x68);
    out.write((char *)reg,0x400);
    out.close();
  }
  
int main(int argc, char* argv[]) {
      
    double start=GetTime();
    cout<<"begining generate..."<<endl;
    GenReg();
    cout<<"done!keyfile successfully created!total time:"<<(GetTime()-start)<<endl;
    cin.get();
    return 0;
}