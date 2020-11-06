#include <iostream>
#include <cmath>
#include <string>
#include <chrono>
#include <ctime>
#include <ncurses.h>
#include <boost/date_time.hpp>

bool checkCustom();
std::string getMonth(int i);
std::string getDay(int i);
std::string getRemedy(int i);
void leki(int dzTygodnia, int dzien);

enum state
{
  menu = 0,
  today = 1,
  enterCustom = 2,
  custom = 3
};

int customY;
int customM;
int customD;

int main()
{
  initscr();
  cbreak();
  keypad(stdscr, TRUE);
  noecho();

  bool looptrue = true;
  state state_ = menu;

  bool error = false;
  std::string lastError = "No error.";

  int opcja;

  std::time_t currentTime = time(0);
  std::tm *currentT = localtime(&currentTime);


  while(looptrue)
  {

    switch(state_)
    {
      case menu:
        if(error)
          mvprintw(0,0, lastError.c_str());

        mvprintw(2,4, "Wybierz opcje:");
        mvprintw(3,6, "1. Dzisiaj");
        mvprintw(4,6, "2. Wlasna Data");
        mvprintw(6,6, "0. Wyjdz");
        refresh();

        opcja = getch() - '0';

        switch(opcja)
        {
          default:
            looptrue = false;
            break;
          case 1:
            state_ = today;
            break;
          case 2:
            state_ = enterCustom;
            break;
        }
        clear();
        break;


      case today:
        error = false;

        mvprintw(2,4, "Dzisiejsza data to: ");
        printw("%d", currentT->tm_mday);
        printw(" ");
        printw(getMonth(currentT->tm_mon + 1).c_str());
        printw(" 2020 r.");
        mvprintw(3,4, "Dzien tygodnia to: ");
        printw(getDay(currentT->tm_wday).c_str());

        leki(currentT->tm_wday, currentT->tm_mday);

        printw("\n\nWcisnij dowolny przycisk, aby wrocic do menu...");
        refresh();
        getch();
        clear();
        state_ = menu;
        break;


      case enterCustom:
        error = false;

        mvprintw(2,2, "Wpisz Rok: XXXX, np 2020");
        refresh();
        customY = 1000*(getch() - '0');
        customY += 100*(getch() - '0');
        customY += 10*(getch() - '0');
        customY += getch() - '0';
        clear();

        mvprintw(2,2,"Wpisz Miesiac: XX, np 06-czerwiec");
        refresh();
        customM = 10*(getch() - '0');
        customM += getch() - '0';
        clear();

        mvprintw(2,2,"Wpisz Dzien: XX, np 03");
        refresh();
        customD = 10*(getch() - '0');
        customD += getch() - '0';
        clear();

        if (checkCustom())
          state_ = custom;
        else
        {
          state_ = menu;
          error = true;
          lastError = "Error: Podana data nie jest prawidlowa.";
        }

        break;


      case custom:
        error = false;
        std::string miesiac = getMonth(customM);
        int index = boost::gregorian::date(customY, customM, customD).day_of_week();

        mvprintw(2,4, "Wybrana data to: ");
        printw("%d",customD);
        printw(" ");
        printw(miesiac.c_str());
        printw(" ");
        printw("%d",customY);
        printw(" r.");
        mvprintw(3,4, "Dzien tygodnia to: ");
        printw(getDay(index).c_str());

        leki(index, customD);

        printw("\n\nWcisnij dowolny przycisk, aby wrocic do menu...");
        refresh();
        getch();
        clear();
        state_ = menu;
        break;
    }
  }

  refresh();
  endwin();
  return 0;
}

bool checkCustom()
{
  int maxDay = 28;
  int minDay = 1;

  if (customM > 12 || customM <= 0 || customD < minDay || customY < 1900 || customY > 2100)
    return false;

  if (customM == 1 || customM == 3 || customM == 5 || customM == 7 || customM == 8 || customM == 10 || customM == 12)
    maxDay = 31;
  else
    maxDay = 30;

  if (customM == 2)
    maxDay = 29;

  if(customD < minDay || customD > maxDay)
    return false;

  return true;
}

std::string getMonth(int i)
{
  switch(i)
  {
    case 1: return "Styczen";
    case 2: return "Luty";
    case 3: return "Marzec";
    case 4: return "Kwiecien";
    case 5: return "Maj";
    case 6: return "Czerwiec";
    case 7: return "Lipiec";
    case 8: return "Sierpien";
    case 9: return "Wrzesien";
    case 10: return "Pazdziernik";
    case 11: return "Listopad";
    case 12: return "Grudzien";
  }
  return " ";
}

std::string getDay(int i)
{
  switch(i)
  {
    case 1: return "poniedzialek";
    case 2: return "wtorek";
    case 3: return "sroda";
    case 4: return "czwartek";
    case 5: return "piatek";
    case 6: return "sobota";
    default: return "niedziela";
  }
  return " ";
}

std::string getRemedy(int i)
{
  const char nearestVowel[26] = "abbbbhhhhhllmmoosssssssss";
  const char j = nearestVowel[i - 1];

  switch(j)
  {
    case 'a': return "Azithromycin";
    case 'b': return "Besylate";
    case 'h': return "Hydrocodone";
    case 'l': return "Lisinopril";
    case 'm': return "Metformin";
    case 'o': return "Omeprazole";
    default: return "Simvastatin";
  }
  return " ";
}

void leki(int dzTygodnia, int dzien)
{
  //Dzien tygodnia - jaki lek?
  std::string dzTyg = getDay(dzTygodnia);
  const char *dzChar = dzTyg.c_str(); 
  int lenght = dzTyg.size();
  int srednia = 0;

  mvprintw(5,6,"Ilosc liter w dniu tygodnia: ");
  printw("%d", lenght);

  for(int i = 0; i < lenght; i++)
  {
    srednia += dzChar[i] - 97;
  }

  srednia = srednia / lenght;
  const char litSr = srednia + 96;
  const char *literaSrednia = &litSr;
  mvprintw(6,6,"Wyliczona srednia wynosi: ");
  printw("%d", srednia);
  mvprintw(7,6,"Srednia odpowiada literze: ");
  printw(literaSrednia);
 
  //Czy i ile musi wziac tabletek
  int ile = 1;
  bool czyTrzeba = false;
  bool warunek1 = false;
  bool warunek2 = false;

  if(dzien % 10)
    czyTrzeba = true; 

  if(15<dzien && dzien<30)
  {
    warunek2 = true;
    ile = 2;
  }

  float sqrtDay = sqrt((float)dzien);
  if(sqrtDay - (int)sqrtDay == 0)
  {
    warunek1 = true;
    ile = (int)sqrtDay;
  }

  mvprintw(9,6, "Spelnione warunki to...");
  mvprintw(10,10, "Wyciagniecie liczby cal. z pierwiastka dnia miesiaca: ");
  if(warunek1)
    printw("TAK.");
  else
    printw("NIE.");

  mvprintw(11,10, "Dzien miesiaca mniejszy od 30 i wiekszy od 15: ");
  if(warunek2)
    printw("TAK.");
  else
    printw("NIE.");

  mvprintw(12,10, "Dzien miesiaca podzielny przez 10: ");
  if(!czyTrzeba)
    printw("TAK.");
  else
    printw("NIE.");

  if(czyTrzeba)
  {
    mvprintw(14,6, "Dzis musi pan wziac lek ");
    printw(getRemedy(srednia).c_str());
    printw(" w ilosci ");
    printw("%d", ile);
    printw(" tabletek.");
  }
  else
  {
    mvprintw(14,6, "Dzisiaj nie musi pan brac zadnych lekow.");
  }
}
