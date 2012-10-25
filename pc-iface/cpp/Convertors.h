/**
  file : #include "Convertors.h"
*/
/*
  Конверторы стандартных типов

  thinks : 
    Для других наверное лучше сделать отдельное простр. 
	  или директивыми управлять
*/

#ifndef _CONVERTORS
#define _CONVERTORS
#include <string>
#include <vector>

// for splitting
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>

namespace Convertors
{
#ifndef _GCC
  std::string CString2string(CString &);
#endif

  std::string replace_with(const std::string & src, const std::string & what, const std::string & with);
  double string2double( const std::string& src);

  ///
  std::string hl(char b1);  // не дороговато ли возвращать строку, может лучше ссылку передать
  std::string hlh(char b1, char b2);  // еще один простейший преобразователь
  std::string lhl(char b1, char b2); 
  void stringProcessing(std::string &s, unsigned int pos);  // xx(pos c 1) = x0x1(,pos)xpos...
  char hbCharToChar(char);  // 0x0y -> char число
  int charToInt(char);  // один символ 
  std::vector<std::string> SplitSpaces( std::string );
}
#endif
