import pyautogui as py
import zlib
from PIL import Image
import time
import os
import random

'''
a = ""
a = zlib.compress(a.encode())
print(zlib.decompress(a).decode())
'''

numere=['0','1','2','3','4','5','6','7','8','9']
quiz=["Se consideră un graf orientat cu 6 vârfuri şi fără circuite. Numărul maxim de arce ale grafului este:","Câte grafuri orientate cu 3 noduri există?","Cate grafuri turneu putem avea formate din 5 noduri?","Cate grafuri complete se pot forma cu 4 noduri?"]
raspuns=["15","32","1024","729"]

#de terminat asta cu quiz urile

#7 9 10 11 13 15 16 17 18 19 25 26 27 29 *30
#1 1 1  1  1  1  1  1  1  1  1  1  1  1   1
optiuni=["exit","1.Defintia 1 graf orientat","2.Definitia 2 graf orientat","3.Definitia 3 graf orientat","4.Extremitati","5.Varfuri adiacente","next->"]
optiuni2=["<-back","6. Arce incidente","7. Bipartit","8. Bucla","9. Grad exterior","10. Grad Interior","next->"]
optiuni3=["<-back","11. Matrice de adiacenta","12. Liste de arce","13. Liste de adiacenta","next->"]
optiuni4=["<-back","14. Graf partial","15. Subgraf","16. Graf Complet","17. Graf Turneu","18. Graf Eulerian","19.Graf Hamiltonian","next->"]
optiuni5=["<-back","20. Lant","21. Ciclu","22. Circuit","23. Drum","24. Nod Izolat","25. Componente Conexe","26. Graf Conex","27. Tare conexitate","next->"]
optiuni6=["<-back","28. Clica","29. Sortare Topologica/ Algoritmul lui Kahn","30. Alogritmul lui Roy-Warshall","Bibliografie","TOP SECRET","exit"]

def q1():
    return py.confirm(text='Introducere in grafuri orientare \n     --------nivel usor:--------', title='Meniul 1 din 6', buttons=optiuni)
def q2():
    return py.confirm(text='Introducere in grafuri orientare \n     --------nivel usor:--------', title='Meniul 2 din 6', buttons=optiuni2)
def q3():
    return py.confirm(text='Reprezentarea grafurilor orientate \n     --------nivel intermediar:--------', title='Meniul 3 din 6', buttons=optiuni3)
def q4():
    return py.confirm(text='Tipuri de grafuri orientate \n     --------nivel intermediar:--------', title='Meniul 4 din 6', buttons=optiuni4)
def q5():
    return py.confirm(text='Proprietati ale grafurilor orientate \n     --------nivel intermediar:--------', title='Meniul 5 din 6', buttons=optiuni5)
def q6():
    return py.confirm(text='Alogritmi avansati pe grafuri orientate \n     --------nivel avansat:--------', title='Meniul 6 din 6', buttons=optiuni6)



def menu1():
  while (1):
    val_q1=q1()
    if (val_q1=="1.Defintia 1 graf orientat"):
        while (1):
            op1=py.confirm(text='1.Definitia 1 graf orientat', title='', buttons=['imagine','text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("1a.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Un graf orientat, sau digraf, este o pereche ordonata de multimi, notata G=(V,E), unde:  V este o multime finita și nevida ale carei elemente se numesc noduri si E este o multime de perechi ordonate de elemente distincte din V, fiecare pereche reprezentand o legatură directionată intre doua noduri si aceasta numindu-se arc.'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("1a.PNG")
                        img.show()
    if (val_q1=="2.Definitia 2 graf orientat"):
        while (1):
            op1=py.confirm(text='2.Definitia 2 graf orientat', title='', buttons=['imagine','text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("1b.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numeste graf orientat o pereche ordonata de multimi notata G=(V, E), unde: V este o multime, finita si nevida, ale carei elemente se numesc noduri; E este o multime, de perechi ordonate de elemente din V, ale carei elemente se numesc arce.\n
*In cadrul definitiei acesteia se introduce notiunea de bucla, vezi 6
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("1b.PNG")
                        img.show()
    if (val_q1=="3.Definitia 3 graf orientat"):
        while (1):
            op1=py.confirm(text='3.Definitia 3 graf orientat', title='', buttons=['imagine','text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("1c.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numeste graf orientat o pereche ordonata de multimi notata G=(V, E), unde: V este o multime, finita si nevida, ale carei elemente se numesc noduri; E este o familie de perechi ordonate de elemente din V, numita familia de arce. Aceasta definitie difera de cea anterioara prin faptul ca acum se admit bucle şi mai multe arce identice.\n
*Dacă într-un graf orientat numărul arcelor identice nu depăşeşte numărul p, atunci se numeşte p-graf.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("1c.PNG")
                        img.show()

    if (val_q1=="4.Extremitati"):
        while (1):
            op1=py.confirm(text='4.Extremitati', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("2.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Pentru un arc (x,y) x reprezinta extremitatea initiala si y extremitatea finala. Definim x ca predecesor a lui y si y succesor al lui x'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("2.PNG")
                        img.show()
    if (val_q1=="5.Varfuri adiacente"):
        while (1):
            op1=py.confirm(text='5.Varfuri adiacente', title='', buttons=['imagine','text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("3.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Daca intre 2 noduri exista cel putin un arc, atunci cele 2 noduri sunt adiacente'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("3.PNG")
                        img.show()
    if (val_q1=="exit"):
        os._exit(1)
    if (val_q1=="next->"):
        menu2()
    
def menu2():
  while (1):
    val_q2=q2()
    if (val_q2=="6. Arce incidente"):
        while (1):
            op1=py.confirm(text='6. Arce incidente', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("4.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Daca 2 arce au una dintre extremitati comuna atunci ele sunt incidente'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("4.PNG")
                        img.show()
    if (val_q2=="7. Bipartit"):
        while (1):
            op1=py.confirm(text='7. Bipartit', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
verificarea daca un graf e sau nu bipartit

int a[102][102], st[102];
int n, m;
int sol = 0 ;

void afisare (){
  if ( sol ){
    fout << "DA" <<endl;
    for ( int i = 1 ; i <= n ; i++ )
      if ( st[i] == 1 )
        fout << i << " " ;
    for ( int i = 1 ; i <= n ; i++ )
      if ( st[i] == 2 )
          fout << i << " " ;
  }
  else
    fout << "NU";
}
int valid ( int k ){
  for ( int i = 1 ; i < k ; i++ )
    if ( st[i] == st[k] && a[i][k] == 1 )
      return 0;
 return 1;
}

void back ( int k ){
  if ( k == n + 1 ){
    sol++;
    return;
  }
  for ( int i = 1 ; i <= 2 && !sol ; i++ ){
     st[k] = i ;
     if ( valid ( k ) )
       back ( k + 1 ) ;
  }
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("5.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("5.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un digraf bipartit este un graf orientat in care multimea nodurilor poate fi impartita in doua multimi disjuncte astfel incat fiecare arc din graf sa pornească dintr-un nod dintr-o multime si sa ajunga la un nod din cealalta multime'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("5.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        elif (chst2=="imagine"):
                            img = Image.open("5.PNG")
                            img.show()
                    
                    
    if (val_q2=="8. Bucla"):
        while (1):
            op1=py.confirm(text='8. Bucla', title='', buttons=['imagine','text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("6.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    In baza definitiei alternative 1, se introduce notiunea de bucla, adica existenta unui arc de tipul (x,x)
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("6.PNG")
                        img.show()
                   

    if (val_q2=="9. Grad exterior"):
        while (1):
            op1=py.confirm(text='9. Grad exterior', title='', buttons=['imagine','cod','text','inapoi'])
            codLOL='''
void citire()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        cin>>x>>y;
        a[x][y]=1;
        de[x]++;
        di[y]++;
    }
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("7.PNG")
                img.show()
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("7.PNG")
                        img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Pentru un graf orientat G=(V,E), se numeste grad exterior al nodului x, numarul arcelor de forma (x,y) (adica numarul arcelor care ies din x), notat de(x)'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("7.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        elif (chst2=="imagine"):
                            img = Image.open("7.PNG")
                            img.show()
    
    if (val_q2=="10. Grad Interior"):
        while (1):
            op1=py.confirm(text='10. Grad Interior', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
void citire()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        cin>>x>>y;
        a[x][y]=1;
        de[x]++;
        di[y]++;
    }
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("8.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("8.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Pentru un graf orientat G=(V,E), Se numeste grad interior al nodului x, numarul arcelor de forma (y,x) (adica numarul arcelor care intra in x), notat di(x).
*Suma gradelor interne coincide cu suma gradelor externe.
'''
                    chst=py.confirm(text='informatii extrem de utile', title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("8.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("8.PNG")
                            img.show()
    if (val_q2=="<-back"):
        menu1()
        break
    if (val_q2=="next->"):
        menu3()
        break


def menu3():
  while (1):
    val_q3=q3()
    if (val_q3=="11. Matrice de adiacenta"):
        while (1):
            op1=py.confirm(text='11. Matrice de adiacenta', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
creearea matricei de adiacenta in memorie

int a[101][101];

int main()
{
    int n,m,x,y,i,j;
    fin>>n>>m;
    for (i=1; i<=m; i++)
    {fin>>x>>y;
    a[x][y]=1;
    }

    for (i=1; i<=n; i++,fout<<endl)
        for (j=1; j<=n; j++)
        fout<<a[i][j]<<" ";

}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("10.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("10.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Fie G=(V,E) un graf orientat cu n noduri, in care nu exista mai multe arce de la un nod la altul. Matricea de adiacenta a grafului este o matrice cu n linii si n coloane si elemente 0 sau 1, astfel: Ai,j=1 daca exista arcul (i,j) Ai,j=0 daca exista nu arcul (i,j).
    Matricea are zerouri pe diagonală (daca în graf nu avem bucle), iar aceasta nu trebuie neaparat să fie simetrică față de diagonala principala.'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("10.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("10.PNG")
                            img.show()
    if (val_q3=="12. Liste de arce"):
        while (1):
            op1=py.confirm(text='12. Liste de arce', title='', buttons=['imagine','text','inapoi'])
            codLOL=''''''
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("11.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Lista de arce a unui graf orientat reprezinta o multime (familie, daca arcele se pot repeta) ce contine toate arcele din graf.
    Pentru reprezentarea in memorie putem folosi: un tablou unidimensional cu elemente de tip struct {int I,J;}, doua tablouri unidimensionale cu elemente de tip int, o lista alocată dinamic etc.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("11.PNG")
                        img.show()
                    
    if (val_q3=="13. Liste de adiacenta"):
        while (1):
            op1=py.confirm(text='13. Liste de adiacenta', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
#include <fstream>

using namespace std;
ifstream fin(".in");
ofstream fout(".out");
int a[1001][1001],n,d[1001],ok,k,cnt;
struct nod
{
    int info;
    nod*urm;
};nod *L[100001];
void adaugare(int x,int y)
{
    nod*p=new nod;
    p->info=y;
    p->urm=L[x];
    L[x]=p;
}

void citire()
{
    fin>>n;
    int x,y;
    while(fin>>x>>y)
    {
        adaugare(x,y);
    }
}

void lad(int x)
{
    nod*p=L[x];
    while(p)
    {
        fout<<p->info<<" ";
        p=p->urm;
    }
    fout<<'\n';
}
int main()
{
    citire();
    for(int i=1;i<=n;i++)
    {
        fout<<i<<": ";
        lad(i);
    }
    return 0;
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("12.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("12.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Pentru un graf orientat cu G=(V,E) se va memora numarul de noduri n si apoi, pentru fiecare nod x, lista succesorilor lui x, adica nodurilor y cu proprietatea ca exista arcul (x,y).\n
    !!ATENTIE!!: dimensiunile listelor de succesori sunt variabile. De aceea, este ineficienta utilizarea unor tablouri alocate static. Astfel, putem folosi: un sir de n tablouri unidimensionale alocate dinamic; un sir de n vectori din STL; un sir de n liste simplu (dublu) inlantuite alocate dinamic.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("12.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("12.PNG")
                            img.show()

    
    if (val_q3=="<-back"):
        menu2()
        break
    if (val_q3=="next->"):
        menu4()
        break


def menu4():
  while (1):
    val_q4=q4()
    if (val_q4=="14. Graf partial"):
        while (1):
            op1=py.confirm(text='14. Graf partial', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("13.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numeste graf partial al grafului G, graful orientat G1=(V, E1), unde E1 ⊆ E. Obs:Un graf partial al unui graf orientat G=(V,E), are aceeasi multime de noduri ca si G, iar multimea arcelor este o submultime a lui E sau chiar E.
    Fie G=(V, E) un graf orientat. Un graf partial al grafului G, se obtine pastrand nodurile si eliminand eventual niste arce (se pot elimina si toate arcele sau chiar nici unul).'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("13.PNG")
                        img.show()
                    
    if (val_q4=="15. Subgraf"):
        while (1):
            op1=py.confirm(text='15. Subgraf', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''subgraf in care se pastreaza doar nodurile cu proprietate de primalitate

int a[1001][1001],n,d[1001],ok,k,cnt;
int prim(int n)
{
    if(n<2) return 0;
    if(n==2) return 1;
    if(n%2==0) return 0;
    for(int i=3;i*i<=n;i+=2)
        if(n%i==0)
            return 0;
    return 1;
}
void citire()
{
    int i,x,y,m;
    fin>>n;
    while(fin>>x>>y)
    {
        if(a[x][y]==0)
            d[x]++,di[y]++;
        a[x][y]=1;
    }
}
int main()
{
    citire();
    int maxx=0;
    for(int i=1; i<=n; i++)
    {
        if(prim(i))
            {for(int j=1; j<=n; j++)
                a[i][j]=0;}
    }
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            if(i!=j && i<j && a[i][j]==1)
                cnt++;
    fout<<cnt;
    return 0;
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("14.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("14.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Fie G=(V, E) un graf orientat. Se numeşte subgraf al grafului G graful orientat G1=(V1,E1) unde V1 ⊆ V iar E1 contine toate arcele din E care au extremitatile în V1. Din definitie rezulta: Fie G=(V,E) un graf orientat.
    Un subgraf al grafului G, se obtine stergand eventual anumite noduri si odata cu acestea şi arcele care le admit ca extremitate (nu se pot sterge toate nodurile deoarece s-ar obtine un graf cu mulțimea nodurilor vidă).'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("14.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        elif (chst2=="imagine"):
                            img = Image.open("14.PNG")
                            img.show()
    if (val_q4=="16. Graf Complet"):
        while (1):
            op1=py.confirm(text='16. Graf Complet', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''int main()
{
    int n,m;
    //n-nr de noduri
    //m-nr de muchii
    cin>>n>>m;
    if (m!=n*(n-1))
        cout<<"NU E COMPLET";
    else
        cout<<"GRAF COMPLET";
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("15.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("15.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Fie G=(V, E) un graf orientat. Graful G se numeste graf complet daca oricare doua noduri distincte ale sale sunt adiacente.'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("15.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("15.PNG")
                            img.show()
    if (val_q4=="17. Graf Turneu"):
        while (1):
            op1=py.confirm(text='17. Graf Turneu', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
determinarea unui drum elementar intr-un graf turneu

int a[101][101],n,viz[101],q[101];

int dfs (int x,int k)
{
q[k]=x;
viz[x]=1;
if (k==n)
{
for (int i=1; i<=n; i++)
    cout<<q[i]<<" ";
exit(0);

}
for (int i=1; i<=n; i++)
if (!viz[i]&&a[x][i])
{dfs(i,k+1);
viz[i]=0;

}

}

int main()
{ int m,k,x,y;
cin>>n;//>>k>>m;
m=n*(n-1)/2;
for (int i=1; i<=m; i++)
    {cin>>x>>y;
    a[x][y]=1;}

dfs(1,1);


}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("16.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("16.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un graf orientat este turneu, dacă oricare ar fi doua noduri şi j, i≠j, intre ele exista un singur arc: arcul (i,j) sau arcul (j,i).'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("16.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("16.PNG")
                            img.show()
    if (val_q4=="18. Graf Eulerian"):
        while (1):
            op1=py.confirm(text='18. Graf Eulerian', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
determina un ciclu eulerian

int a[1001][1001],gr[1001],lg=0;
int viz[10001],n;

int dfs(int st)
{
gr[st]--;
for (int i=1; i<=n; i++)
    if (gr[i]!=0&&a[i][st]==1)
    {
    a[i][st]=0;
    a[st][i]=0;
    dfs(i);

 }
fout<<st<<" ";
}

int main()
{
    int m=0,x,y,i;
    fin>>n;
    while (fin>>x>>y)
    {
    a[x][y]=1;
    a[y][x]=1;
    m++;
    }
    for (int i=1; i<=n; i++)
    {int s=0;
    for (int j=1; j<=n; j++)
            s+=a[i][j];
    gr[i]=s;
    }
    fout<<m+1<<endl;
    dfs(1);
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("17.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("17.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un drum care contine toate arcele grafului se numeste drum eulerian. Un circuit care contine toate arcele grafului se numeste circuit eulerian. Un graf care contine un circuit eulerian se numeste graf eulerian. 
    * Un graf fara noduri izolate este eulerian daca și numai daca este conex si pentru fiecare nod, gradul interior este egal cu cel exterior.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("17.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("17.PNG")
                            img.show()

    if (val_q4=="19.Graf Hamiltonian"):
        while (1):
            op1=py.confirm(text='19.Graf Hamiltonian', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
determina un ciclu hamiltonian din graf

int sel[101],v[101],n,a[101][101],use[101],altv[101],m;
bool ok=0;

int afisare(int k)
{
if (a[v[1]][v[k]]==0)
    return 0;
    ok=1;
for (int i=1; i<=k; i++)
    altv[i]=v[i];
altv[k+1]=v[1];
m=k+1;
}

int val (int k)
{
if (k==1)
    return 1;
if (a[v[k-1]][v[k]]==0)
    return 0;
else
    return 1;
}

void bkt(int k)
{
for (int i=1; i<=n; i++)
    if (use[i]==0)
{
    v[k]=i;
    use[i]=1;
        if (val(k))
            if (k==n)
                afisare(k);
        else
            bkt(k+1);
    use[i]=0;
}
}

int main()
{
    int x,y;
    fin>>n;
while (fin>>x>>y)
a[x][y]=1;
    bkt(1);
    if (ok==1)
    {
    fout<<1<<'\n';
    for (int i=1; i<=m; i++)
        fout<<altv[i]<<" ";
    }
    else 
        fout<<'0';
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("18.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("18.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un drum elementar care contine toate nodurile grafului se numeste drum hamiltonian. 
    Un circuit elementar care contine toate nodurile grafului se numeste circuit hamiltonian. 
    Un graf care contine un circuit hamiltonian se numeste graf hamiltonian.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("18.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("18.PNG")
                            img.show()
    if (val_q4=="<-back"):
        menu3()
        break
    if (val_q4=="next->"):
        menu5()
        break


def menu5():
  while (1):
    val_q5=q5()
    if (val_q5=="20. Lant"):
        while (1):
            op1=py.confirm(text='20. Lant', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("19.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Fie G=(V, E) un graf orientat. Se numește lant, in graful G, o succesiune de arce, notata L = (u1 , u2 ,..., uk) cu proprietatea ca oricare două arce consecutive au o extremitate comuna (nu are importanta orientarea arcelor).
    Lungimea unui lant este egala cu numarul de arce din care este alcatuit. Primul nod si ultimul nod dintr-un lant formeaza extremitatile lantului.
    Un lant se numeste elementar daca in el nu se repeta noduri. Un lant se numeste simplu daca in el nu se repeta arce.
'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("19.PNG")
                        img.show()
    if (val_q5=="21. Ciclu"):
        while (1):
            op1=py.confirm(text='21. Ciclu', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("20.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numește ciclu un lant simplu in care primul vârf este identic cu ultimul. Daca toate nodurile sunt distincte, mai putin primul si ultimul, se numeste ciclu elementar.
    Lungimea unui ciclu este egala cu numarul de arce din ciclu. Lungimea minima a unui ciclu este 3. Un ciclu se numeste par daca lungimea sa este para, respectiv impar in caz contrar.'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("20.PNG")
                        img.show()
    if (val_q5=="22. Circuit"):
        while (1):
            op1=py.confirm(text='22. Circuit', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("21.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numeste circuit un drum simplu in care extremitatea initială si finala sunt egale.
    Se numeste circuit elementar un circuit in care, cu exceptia extremitatilor, nu se repetă noduri.
    Lungimea unui circuit este reprezentată de numărul de arce din care acesta este alcătuit.'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("21.PNG")
                        img.show()

    if (val_q5=="23. Drum"):
        while (1):
            op1=py.confirm(text='23. Drum', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("22.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Definitia 1: Se numeste drum in graful G o succesiune de noduri, notată D = (x1 , x2 ,..., xk), cu proprietatea ca pentru orice 1≤i<k, (xi,xi+1) este arc in G. Lungimea unui drum este egala cu numarul de arce din care este alcatuit. Pentru un drum D = (x1 , x2 ,..., xk), nodurile x1 și xk reprezinta extremitatile – initiala, respectiv finala.
    Definitia 2: Un drum se numeste elementar daca in el nu se repeta noduri. Un drum se numeste simplu daca in el nu se repeta arce.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("22.PNG")
                        img.show()
    if (val_q5=="24. Nod Izolat"):
        while (1):
            op1=py.confirm(text='24. Nod Izolat', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("9.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un nod x se numeste izolat dacă de(x)=di(x)=0 (are gradul interior si gradul exterior egal cu 0).'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("9.PNG")
                        img.show()
    if (val_q5=="25. Componente Conexe"):
        while (1):
            op1=py.confirm(text='25. Componente Conexe', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''int a[101][101],viz[101],n,m,q[101],cntr,k,vec[101];

void DFS (int start)
{
if (viz[start]==0)
        cntr++;
viz[start]=1;
for (int i=1; i<=n; i++)
    if (!viz[i]&&a[start][i]==1)
    DFS(i);
}
void DFS1 (int start)
{
if (viz[start]==0)
        {vec[k]=start,k++,cntr++;
}
viz[start]=1;
for (int i=1; i<=n; i++)
    if (!viz[i]&&a[start][i]==1)
    DFS1(i);
}

int main()
{ int sta,s=0;
    fin>>n;
    int x,y;
while (fin>>x>>y)
{
a[x][y]=1;
a[y][x]=1;
}
for (int i=1; i<=n; i++)
    {   cntr=0;
        DFS(i);
        if (cntr)
        s++;
    }
    fout<<s<<endl;
for (int i=1; i<=n; i++)
    viz[i]=0;
for (int i=1; i<=n; i++)
    {   cntr=0,k=1;
        DFS1(i);
    sort(vec+1,vec+k);
    for (int j=1; j<=k-1; j++)
        fout<<vec[j]<<" ";
    if (k!=1)
    fout<<endl;
    }
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):  
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("23.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("23.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Se numeste componenta conexa a unui graf G=(X,E) un subgraf H=(Y, V), conex, al lui G care are proprietatea ca nu exista nici un lant în G care sa lege un varf din Y cu un varf din X – Y.
    Subgraful H este conex si maximal cu aceasta proprietate (daca s-ar mai adauga un varf nu ar mai fi conex.) Un graf este conex daca admite o singura componentă conexa.'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("23.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("23.PNG")
                            img.show()
    if (val_q5=="26. Graf Conex"):
        while (1):
            op1=py.confirm(text='26. Graf Conex', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
verifica daca graful este sau nu conex

int a[101][101],viz[101],n,m,q[101];

void BFS (int start )
{
int st,dr,i,x;
q[1]=start;
viz[start]=1;
st=dr=1;
fout<<start<<" ";
while (st<=dr)
    {x=q[st];
    st++;
    for (i=1; i<=n; i++)
        if (!viz[i]&&a[x][i]==1)
    {viz[i]=1;
    q[++dr]=i;
    fout<<i<<" ";
    }
    }
}

void DFS (int start)
{
viz[start]=1;
for (int i=1; i<=n; i++)
    if (!viz[i]&&a[start][i]==1)
    DFS(i);
}

int main()
{ int sta;
    fin>>n;
    int x,y;
while (fin>>x>>y)
{
a[x][y]=1;
}
DFS(1);
for (int i=1; i<=n; i++)
    if (viz[i]==0)
    {fout<<"NU";
return 0;}
fout<<"DA";
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("25.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("25.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Un graf orientat se numeste graf conex daca pentru oricare doua noduri x și y diferite ale sale, exista cel putin un lant care le leaga, adica x este extremitatea initiala și y este extremitatea finala.'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("25.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("25.PNG")
                            img.show()
    if (val_q5=="27. Tare conexitate"):
        while (1):
            op1=py.confirm(text='27. Tare conexitate', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
determina cate componente tari conexe are graful

int N , M , X , Y , c , ctc[101];

bool a[101][101] , S[101] , P[101];
void DFS (int V)
{
    S[V] = 1;
    for(int i = 1; i <= N; ++i)
        if(!S[i] && a[V][i])
            DFS(i);
}

void DFS1 (int V)
{
    P[V] = 1;
    for(int i = 1; i <= N; ++i)
        if(!P[i] && a[i][V])
            DFS1(i);
}

int main()
{
    cin >> N >> M;
    while(M --)
    {
        cin >> X >> Y;
        a[X][Y] = 1;
    }
    for(int i = 1; i <= N; ++i)
        if(ctc[i] == 0)
        {
            DFS(i);
            DFS1(i);
            ++c;
            ctc[i] = c;
            for(int j = 1; j <= N; ++j)
            {
                if(S[j] && P[j])
                    ctc[j] = c;
                S[j] = P[j] = 0;
            }
        }
    cout << c;
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("25.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("25.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Graful se numeste tare conex daca intre oricare doua noduri distincte exista cel putin un drum.
    Se numeste componenta tare conexa un subgraf tare conex si maximal cu aceasta calitate – daca am mai adauga un nod, n-ar mai fi tare conex.
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("25.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("25.PNG")
                            img.show()
    if (val_q5=="<-back"):
        menu4()
        break
    if (val_q5=="next->"):
        menu6()
        break
    #if (val_q5=="TOP SECRET")
    #ar merge cv sistem bazat pe cautarea unui cod in interiorul programului si introudcerea lui in top secret pentru o diploma

def menu6():
  while (1):
    val_q6=q6()
    if (val_q6=="28. Clica"):
        while (1):
            op1=py.confirm(text='28. Clica', title='', buttons=['imagine', 'text','inapoi'])
            if (op1=="inapoi"):
                break
            elif (op1=="imagine"):
                img = Image.open("24.PNG")
                img.show()
            elif (op1=="text"):
                textLOL='''    Se defineste o clica intr-un graf orientat ca fiind o submultime de noduri U a multimii V, asfel ca intre oricare doua noduri u şi v ale lui U exista un arc orientat fie de la u la v, fie invers de la v la u (sau ambele).
    Dimensiunea unei clici U este numărul de noduri ale clicii.'''
                while (1):
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("24.PNG")
                        img.show()
    if (val_q6=="29. Sortare Topologica/ Algoritmul lui Kahn"):
        while (1):
            op1=py.confirm(text='29. Sortare Topologica/ Algoritmul lui Kahn', title='', buttons=['imagine','cod', 'text','inapoi'])
            codLOL='''
#define N 100010
#define M 400010
int start[N], a[2][M], q[N], n, k, cate;
bool viz[N];
void dfs(int x)
{
    viz[x]=1;
    for(int poz=start[x]; poz!=0; poz=a[1][poz])
        if(viz[a[0][poz]]==0)
            dfs(a[0][poz]);
    q[++cate]=x;
}int main()
{
    int m, i, x, y;
    f>>n>>m;
    for(i=1;i<=m;i++)
    {
        f>>x>>y;
        k++;
        a[0][k]=y;
        a[1][k]=start[x];
        start[x]=k;
    }
    for(i=1;i<=n;i++)
        if(viz[i]==0)
        dfs(i);
    for(i=cate;i>=1;i--)
        g<<q[i]<<' ';
    return 0;
}'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=="imagine"):
                            img = Image.open("27.PNG")
                            img.show()
            elif (op1=="imagine"):
                            img = Image.open("27.PNG")
                            img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    O sortare topologica a nodurilor unui graf orientat aciclic este o operatie de ordonare liniara a nodurilor, astfel incat, daca exista un arc ( i , j ), atunci i apare inaintea lui j in aceasta ordonare. Pe scurt, sortarea topologica sorteaza nodurile astfel incat fiecare sa apara inaintea celui catre care indica.
    Sortarea topologica se poate aplica doar daca graful orientat (numit si digraf) care se construieste pe baza datelor si a relatiilor dintre acestea este aciclic.
    Algoritmul de sortare topologică are la baza gradul intern al fiecarui nod al grafului. Se porneste de la nodurile care au gradul intern zero si se vor adauga pe parcurs acele noduri, pentru care gradul intern devine zero.
    Algoritmul poate fi implementat si static si dinamic
'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("27.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("27.PNG")
                            img.show()

    if (val_q6=="30. Alogritmul lui Roy-Warshall"):
        while (1):
            op1=py.confirm(text='30. Alogritmul lui Roy-Warshall', title='', buttons=['imagine', 'cod','text','inapoi'])
            codLOL='''
for(int k = 1 ; k <= n ; ++k)
    for(int i = 1 ; i <= n ; ++i)
        for(int j = 1 ; j <= n ; ++j)
            if( i != j && a[i][j] == 0 &&  a[i][k] == 1 && a[k][j] == 1)
                a[i][j] = 1;'''
            if (op1=="inapoi"):
                break
            elif (op1=="cod"):
                while (1):
                    chst=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                    if (chst=='inapoi'):
                        break
                    elif (chst=="imagine"):
                        img = Image.open("28.PNG")
                        img.show()
            elif (op1=="imagine"):
                img = Image.open("28.PNG")
                img.show()
            elif (op1=="text"):
                while (1):
                    textLOL='''    Matricea de drumuri a unui graf orientat este o matrice de dimensiuni n*n, unde n este numarul de noduri din graf. Elementele matricei sunt asociate lungimile drumurilor dintre noduri.
    Daca nu exista o legatura intre 2 noduri, valoarea corespunzatoare in matrice este infinit. Aceasta matrice este esentiala in algoritmi precum Roy-Floyd.'''
                    chst=py.confirm(text=textLOL, title='',buttons=['imagine','cod','inapoi'])
                    if (chst=='inapoi'):
                        break
                    if (chst=='imagine'):
                        img = Image.open("28.PNG")
                        img.show()
                    elif (chst=="cod"):
                     while (1):
                        chst2=py.confirm(text=codLOL,title='',buttons=['imagine','inapoi'])
                        if (chst2=='inapoi'):
                            break
                        
                        elif (chst2=="imagine"):
                            img = Image.open("28.PNG")
                            img.show()
    if (val_q6=="TOP SECRET"):
        while (1):
            nr_de_optiuni=4
            nr=random.randrange(0,nr_de_optiuni,1)
            vals=py.password(text=quiz[nr],title='',default='',mask='')
            if (vals==""):
                break
            if (vals==None):
                break
            if (vals==raspuns[nr]):
                img = Image.open("diploma.jpg")
                img.show()
                break
            else:
                py.alert(text='Ai raspuns gresit la intrebare, incearca din nou', title='' ,button='OK')
                break
    if (val_q6=="Bibliografie"):
        while (1):
            textLOL='''
documentatie text:
 https://www.pbinfo.ro/
 https://www.infoarena.ro/
 https://revista.infobits.ro/2022/01/13/sortare-topologica

documentatie cod:
 https://pyautogui.readthedocs.io/en/latest/msgbox.html


'''
            var1111=py.alert(text=textLOL, title='Bibliografie' ,button='Inapoi')
            if (var1111=='Inapoi'):
                break
    if (val_q6=="<-back"):
        menu5()
        break
    if (val_q6=="exit"):
        os._exit(1)
        break
    
while (1):
    textLOL='''
MENIU DE AJUTOR
        * navigheaza meniurile principale cu ajutorul butoanelor:
        * next-> pt a trece la urmatorul
        * <-back pt a trece la meniul anterior
        * foloseste exit pentru a iesi din program
        * fiecare item (de la 1 la 30) are un submeniu asociat, in care se pot gasi: o imagine, textul aferent si cod (daca este cazul)
        * navigheaza exclusiv cu ajutorul butoanelor din INTERIORUL PROGRAMULUI

'''
    var11=py.confirm(text=textLOL, title='AJUTOR', buttons=['Continua spre program', 'Exit'])
    if (var11=='Continua spre program'):
        menu1()
    else:
        break
        os.exit(1)

