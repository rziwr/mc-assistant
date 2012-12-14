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
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently,
// but are changed infrequently

#pragma once

#ifndef _SECURE_ATL
#define _SECURE_ATL 1
#endif

#ifndef VC_EXTRALEAN
#define VC_EXTRALEAN            // Exclude rarely-used stuff from Windows headers
#endif

//#include "targetver.h"

#define _ATL_CSTRING_EXPLICIT_CONSTRUCTORS      // some CString constructors will be explicit

// turns off MFC's hiding of some common and often safely ignored warning messages
#define _AFX_ALL_WARNINGS

#include <afxwin.h>         // MFC core and standard components
#include <afxext.h>         // MFC extensions


#include <afxdisp.h>        // MFC Automation classes



#ifndef _AFX_NO_OLE_SUPPORT
#include <afxdtctl.h>           // MFC support for Internet Explorer 4 Common Controls
#endif
#ifndef _AFX_NO_AFXCMN_SUPPORT
#include <afxcmn.h>                     // MFC support for Windows Common Controls
#endif // _AFX_NO_AFXCMN_SUPPORT


#include <afxsock.h>            // MFC socket extensions

#define _WIN32_DCOM 
//#define	DONT_SHOW_NOSYNC


#define		USE_EFW

// App cfg.
#define CODE_USE


#ifdef _UNICODE
#if defined _M_IX86
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='x86' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_IA64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='ia64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#elif defined _M_X64
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='amd64' publicKeyToken='6595b64144ccf1df' language='*'\"")
#else
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")
#endif
#endif

// конфигурации
//#define NEVA2RTS


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
