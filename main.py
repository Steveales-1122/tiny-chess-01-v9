import os,json,urllib.request as r
V=(0,100,320,330,500,900,0);O=(1,-1,16,-16,17,15,-17,-15);J=(31,33,14,18,-31,-33,-14,-18)
b=[0]*256;Z=[1,15,-1];K=[4,116];N=[0];B=100000;Kl=[[0,0]for _ in range(32)]
class E(Exception):pass
P=[2-max(abs(q%8-3.5),abs(q//16-3.5))for q in range(128)]
def A(q,t):
 u=6*(t<0)
 for i,o in enumerate(J+O):
  if b[q+o]==(2+u if i<8 else 6+u):return 1
 if 1+u in(b[q-16*t-1],b[q-16*t+1]):return 1
 for i,o in enumerate(O):
  x=q+o
  while not x&136:
   p=b[x]
   if p:
    if p-u in((4,5)if i<4 else(3,5)):return 1
    break
   x+=o
 return 0
def I():return A(K[Z[0]>0],Z[0])
def G():
 m=[];w=Z[0]>0
 for s in range(128):
  p=b[s]
  if s&136 or not p or(p<7)!=w:continue
  a=(p-1)%6+1
  if a==1:
   d=32*w-16;e=s+d;pm=81920*(s>>4==5*w+1)
   if not b[e]:
    m.append(s*128+e+pm)
    if s>>4==6-5*w and not b[e+d]:m.append(s*128+e+d)
   for q in(e-1,e+1):
    if b[q]and(b[q]<7)!=w:m.append(s*128+q+pm)
    elif q==Z[2]:m.append(s*128+q)
  else:
   oo=(0,0,J,O[4:],O[:4],O,O)[a]
   for o in oo:
    q=s+o
    while not q&136:
     if b[q]:
      if(b[q]<7)!=w:m.append(s*128+q)
      break
     m.append(s*128+q)
     if a in(2,6):break
     q+=o
 k=116-112*w
 for d in(1,-1):
  bit=(2-(d>0))*(4-3*w);rs=k+3*d-(d<0)
  if Z[1]&bit and b[rs]==10-6*w and not(b[k+d]or b[k+2*d]or(d<0 and b[k+3*d]))and not any(A(k+i*d,-Z[0])for i in range(3)):m.append(k*128+k+2*d)
 return m
def D(mv):
 c=mv&127;a=mv>>7&127;p=mv>>14;pc=b[a];w=pc<7;cap=b[c];ec=-1;rf=-1;rt=-1
 if pc%6==0 and abs(c-a)==2:
  rf=a+3-7*(c<a);rt=rf-2+5*(c<a);b[rt]=b[rf];b[rf]=0
 if pc%6==1 and c==Z[2]and not cap:
  ec=c-16*(2*w-1);cap=b[ec];b[ec]=0
 b[c]=p+6*(not w)if p else pc;b[a]=0
 ep=a+16*(2*w-1)if pc%6==1 and abs(c-a)==32 else-1
 n=Z[1]
 if pc%6==0:n&=3+9*(pc<7)
 for q,v in((0,2),(7,1),(112,8),(119,4)):
  if a==q or c==q:n&=~v
 o=Z[:];Z[:]=-Z[0],n,ep
 if pc%6==0:K[pc>6]=c
 return(cap,o,ec,rf,rt)
def U(mv,u):
 c=mv&127;a=mv>>7&127;p=mv>>14;cap,o,ec,rf,rt=u;pc=b[c]
 if p:pc=1+6*(pc>6)
 b[a]=pc
 if ec>=0:b[ec]=cap;b[c]=0
 else:b[c]=cap
 if rf>=0:b[rf]=b[rt];b[rt]=0
 Z[:]=o
 if pc%6==0:K[pc>6]=a
def Ev():
 s=0;m=0
 for q in range(128):
  p=b[q]
  if q&136 or not p:continue
  a=(p-1)%6+1;w=p<7;v=V[a];m+=v
  if a==6:continue
  s+=(v+5*P[q^112*(1-w)])*(2*w-1)
  if a==1:
   r=q>>4;s+=4*(r-7*(not w))
 f=10 if m<2400 else-6;s+=(P[K[0]]-P[K[1]^112])*f
 return s if Z[0]>0 else-s
def C(x):return b[x&127]*100-b[x>>7&127]
def S(d,al,be):
 N[0]+=1
 if N[0]>B:raise E
 w=Z[0]>0;ck=A(K[1-w],-Z[0])
 if d<=0:
  s=Ev()
  if s>=be:return s
  if s>al:al=s
  if d<-10:return al
 elif ck:d+=1
 ms=G()
 if d<=0 and not ck:ms=[x for x in ms if b[x&127]or x>>14]
 ms.sort(key=lambda x:-(9000*(x in Kl[d])+C(x)))
 bs=-99999
 for mv in ms:
  u=D(mv)
  if I():U(mv,u);continue
  s=-S(d-1,-be,-al);U(mv,u)
  if s>bs:bs=s
  if s>al:al=s
  if al>=be:
   if d>0 and not b[mv&127]:Kl[d][1]=Kl[d][0];Kl[d][0]=mv
   break
 if d<=0:return-100000 if ck and bs==-99999 else al
 if bs==-99999:return-100000 if ck else 0
 return bs
def R():
 ms=G();L=[]
 for mv in ms:
  u=D(mv)
  if not I():L.append(mv)
  U(mv,u)
 L.sort(key=lambda x:-C(x));best=L[0];N[0]=0
 for d in range(1,9):
  try:
   if best in L:L.remove(best);L.insert(0,best)
   lb=L[0];ls=-9**9
   for mv in L:
    u=D(mv);s=-S(d-1,-9**9,-ls);U(mv,u)
    if s>ls:ls=s;lb=mv
   best=lb
  except E:break
 return best
def X(mv):
 y=lambda q:chr(97+(q&7))+str(q//16+1)
 return y(mv>>7&127)+y(mv&127)+'q'*(mv>>14>0)
def L(p,d):return json.load(r.urlopen(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(d).encode(),timeout=9))
while 1:
 try:g=L('/game',{})
 except Exception:continue
 t=g.get('status')
 if t=='done':break
 if t!='your_move':continue
 n=g['game']
 try:
  ms=g['moves'];b=[0]*256;Z[0]=1;Z[1]=15;Z[2]=-1;K[0]=4;K[1]=116
  for i,v in enumerate((4,2,3,5,6,3,2,4)):b[i]=v;b[i+112]=v+6;b[i+16]=1;b[i+96]=7
  q=lambda s:ord(s[0])+ord(s[1])*16-881
  for m in ms:
   a=q(m[:2]);c=q(m[2:]);p=5-"qrbn".index(m[4])if len(m)>4 else 0;D(a*128+c+(p<<14))
  mv=R()
  if mv:L('/move',{'game':n,'move':X(mv)})
 except Exception:pass
