<<<<<<< HEAD
#include "Convertors.h"
using namespace std;
using namespace Convertors;

#ifndef _GCC

std::string Convertors::CString2string(CString &CStringIn) {
  CT2CA pszConvertedAnsiString(CStringIn);
  string PortName(pszConvertedAnsiString);
  return PortName;

}
#endif
///
string Convertors::replace_with( const std::string & src, const std::string & what, const std::string & with)
{    
	string result = src;
    if (what != with) {
        std::string temp;
        std::string::size_type prev_pos = 0, pos = result.find(what, 0);
        while ( std::string::npos != pos ) {
            temp += std::string(result.begin() + prev_pos, result.begin() + pos) + with;
            prev_pos = pos + what.size();
            pos = result.find(what, prev_pos);
        }
        if ( !temp.empty() ) {
            result = temp + std::string(result.begin() + prev_pos, result.end());
            if (std::string::npos == with.find(what)) {
                result = Convertors::replace_with(result, what, with);
            }
        }
    }
	return result;
}
///
double Convertors::string2double(const std::string &src) 
{
	// ���� ���� ������ ������� �� �����
	string strTmp = Convertors::replace_with(src, ",", ".");

	// ����������� � ���������� ������� ��������
	double dA = ::strtod( strTmp.c_str(), NULL );
	return dA;
}
///
void Convertors::stringProcessing(std::string &s, unsigned int pos) {
  // ��������� �������
  if(pos != 0)
    s.insert(pos, ",");
  else 
    pos = s.size();

  // ������� �������� ����
  string::iterator ini(s.begin());
  for(unsigned int i = 0; i < pos-1; i++) {
    if(*s.begin() == '0') 
      s.erase(ini);
    else break;
  }
}
//
char Convertors::hbCharToChar(char tmp) {
  char out = '\0';
  tmp &= 0x0f; // �� ������ ������
  switch(tmp) {  // 0-15 - ������ ��������
    case 0 : { out = '0'; } break;
    case 1 : { out = '1'; } break;
    case 2 : { out = '2'; } break;
    case 3 : { out = '3'; } break;
    case 4 : { out = '4'; } break;
    case 5 : { out = '5'; } break;
    case 6 : { out = '6'; } break;
    case 7 : { out = '7'; } break;
    case 8 : { out = '8'; } break;
    case 9 : { out = '9'; } break;
    case 10 : { out = 'A'; } break;
    case 11 : { out = 'B'; } break;
    case 12 : { out = 'C'; } break;
    case 13 : { out = 'D'; } break;
    case 14 : { out = 'E'; } break;
    case 15 : { out = 'F'; } break;
    default : {} break;
  }

  ///
  return out;
}
//////////
std::string Convertors::hl(char b1){ 
  char tmp(b1);
  tmp >>= 4; tmp &= 0x0f;
  ///
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b1; tmp &= 0x0f;
  s.push_back(hbCharToChar(tmp));
  
  //
  return s;
}
std::string Convertors::hlh(char b1, char b2) 
{
  char tmp(b1);
  tmp >>= 4; tmp &= 0x0f;  // ������� ��������
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b1; tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));
  tmp = b2;
  tmp >>= 4; tmp &= 0x0f;  // ������� �������� �������
  s.push_back(hbCharToChar(tmp));

  //
  return s;
}
std::string Convertors::lhl(char b1, char b2){
  char tmp(b1);
  tmp &= 0x0f;  // ������� �������� �������
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b2; 
  tmp >>= 4; tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));
  tmp = b2;
  tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));

  //
  return s;
}
int Convertors::charToInt(char cTmp_0) {
  int Itog = 0;
    char cTmp_1 = cTmp_0;
  cTmp_1 %= 16; cTmp_1 &= 0x0f;
  Itog = static_cast<int>(cTmp_1);  // 0-16
  cTmp_1 = cTmp_0; cTmp_1 >>= 4; cTmp_1 &= 0x0f;
  Itog += (16*static_cast<int>(cTmp_1)); 
  return Itog;
}

std::vector<std::string> Convertors::SplitSpaces( std::string str ) {
	vector<string> tokens;
	istringstream iss( str );
	copy(istream_iterator<string>(iss),
         istream_iterator<string>(),
         back_inserter<vector<string> >(tokens));
	return tokens;
}
=======
#include "Convertors.h"
using namespace std;
using namespace Convertors;

#ifndef _GCC

std::string Convertors::CString2string(CString &CStringIn) {
  CT2CA pszConvertedAnsiString(CStringIn);
  string PortName(pszConvertedAnsiString);
  return PortName;

}
#endif
///
string Convertors::replace_with( const std::string & src, const std::string & what, const std::string & with)
{    
	string result = src;
    if (what != with) {
        std::string temp;
        std::string::size_type prev_pos = 0, pos = result.find(what, 0);
        while ( std::string::npos != pos ) {
            temp += std::string(result.begin() + prev_pos, result.begin() + pos) + with;
            prev_pos = pos + what.size();
            pos = result.find(what, prev_pos);
        }
        if ( !temp.empty() ) {
            result = temp + std::string(result.begin() + prev_pos, result.end());
            if (std::string::npos == with.find(what)) {
                result = Convertors::replace_with(result, what, with);
            }
        }
    }
	return result;
}
///
double Convertors::string2double(const std::string &src) 
{
	// ���� ���� ������ ������� �� �����
	string strTmp = Convertors::replace_with(src, ",", ".");

	// ����������� � ���������� ������� ��������
	double dA = ::strtod( strTmp.c_str(), NULL );
	return dA;
}
///
void Convertors::stringProcessing(std::string &s, unsigned int pos) {
  // ��������� �������
  if(pos != 0)
    s.insert(pos, ",");
  else 
    pos = s.size();

  // ������� �������� ����
  string::iterator ini(s.begin());
  for(unsigned int i = 0; i < pos-1; i++) {
    if(*s.begin() == '0') 
      s.erase(ini);
    else break;
  }
}
//
char Convertors::hbCharToChar(char tmp) {
  char out = '\0';
  tmp &= 0x0f; // �� ������ ������
  switch(tmp) {  // 0-15 - ������ ��������
    case 0 : { out = '0'; } break;
    case 1 : { out = '1'; } break;
    case 2 : { out = '2'; } break;
    case 3 : { out = '3'; } break;
    case 4 : { out = '4'; } break;
    case 5 : { out = '5'; } break;
    case 6 : { out = '6'; } break;
    case 7 : { out = '7'; } break;
    case 8 : { out = '8'; } break;
    case 9 : { out = '9'; } break;
    case 10 : { out = 'A'; } break;
    case 11 : { out = 'B'; } break;
    case 12 : { out = 'C'; } break;
    case 13 : { out = 'D'; } break;
    case 14 : { out = 'E'; } break;
    case 15 : { out = 'F'; } break;
    default : {} break;
  }

  ///
  return out;
}
//////////
std::string Convertors::hl(char b1){ 
  char tmp(b1);
  tmp >>= 4; tmp &= 0x0f;
  ///
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b1; tmp &= 0x0f;
  s.push_back(hbCharToChar(tmp));
  
  //
  return s;
}
std::string Convertors::hlh(char b1, char b2) 
{
  char tmp(b1);
  tmp >>= 4; tmp &= 0x0f;  // ������� ��������
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b1; tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));
  tmp = b2;
  tmp >>= 4; tmp &= 0x0f;  // ������� �������� �������
  s.push_back(hbCharToChar(tmp));

  //
  return s;
}
std::string Convertors::lhl(char b1, char b2){
  char tmp(b1);
  tmp &= 0x0f;  // ������� �������� �������
  string s;
  s.push_back(hbCharToChar(tmp));
  tmp = b2; 
  tmp >>= 4; tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));
  tmp = b2;
  tmp &= 0x0f;  // ������� �������
  s.push_back(hbCharToChar(tmp));

  //
  return s;
}
int Convertors::charToInt(char cTmp_0) {
  int Itog = 0;
    char cTmp_1 = cTmp_0;
  cTmp_1 %= 16; cTmp_1 &= 0x0f;
  Itog = static_cast<int>(cTmp_1);  // 0-16
  cTmp_1 = cTmp_0; cTmp_1 >>= 4; cTmp_1 &= 0x0f;
  Itog += (16*static_cast<int>(cTmp_1)); 
  return Itog;
}

std::vector<std::string> Convertors::SplitSpaces( std::string str ) {
	vector<string> tokens;
	istringstream iss( str );
	copy(istream_iterator<string>(iss),
         istream_iterator<string>(),
         back_inserter<vector<string> >(tokens));
	return tokens;
}

std::wstring Convertors::StringToWString(const std::string& s)
 {
	 std::wstring temp(s.length(),L' ');
	 std::copy(s.begin(), s.end(), temp.begin());
	 return temp; 
 }


 std::string Convertors::WStringToString(const std::wstring& s)
 {
	 std::string temp(s.length(), ' ');
	 std::copy(s.begin(), s.end(), temp.begin());
	 return temp; 
 }


 std::wstring Convertors::Utf8ToUtf16(const std::string &s)
{
    std::wstring ret;
    int len = MultiByteToWideChar(CP_UTF8, 0, s.c_str(), s.length(), NULL, 0);
    if (len > 0)
    {
      ret.resize(len);
      MultiByteToWideChar(CP_UTF8, 0, s.c_str(), s.length(), const_cast<wchar_t*>(ret.c_str()), len);
    }
    return ret;
}

std::string Convertors::Utf16ToUtf8(const std::wstring &s)
{
    std::string ret;
    int len = WideCharToMultiByte(CP_UTF8, 0, s.c_str(), s.length(), NULL, 0, NULL, NULL);
    if (len > 0)
    {
      ret.resize(len);
      WideCharToMultiByte(CP_UTF8, 0, s.c_str(), s.length(), const_cast<char*>(ret.c_str()), len, NULL, NULL);
    }
    return ret;
}

std::wstring Convertors::ANSIToUtf16(const std::string &s)
{
    std::wstring ret;
    int len = MultiByteToWideChar(CP_ACP, 0, s.c_str(), s.length(), NULL, 0);
    if (len > 0)
    {
      ret.resize(len);
      MultiByteToWideChar(CP_ACP, 0, s.c_str(), s.length(), const_cast<wchar_t*>(ret.c_str()), len);
    }
    return ret;
}
std::string Convertors::Utf16ToANSI(const std::wstring &s)
{
    std::string ret;
    int len = WideCharToMultiByte(CP_ACP, 0, s.c_str(), s.length(), NULL, 0, NULL, NULL);
    if (len > 0)
    {
      ret.resize(len);
      WideCharToMultiByte(CP_ACP, 0, s.c_str(), s.length(), const_cast<char*>(ret.c_str()), len, NULL, NULL);
    }
    return ret;
}



>>>>>>> 2baccfef8885a6e8792b41bce568e5ed8f8e5368
