//http://evlz{url_seems_rotten_with_64}.com

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>

char rfc3986[256] = {0};
char html5[256] = {0};
char *flag_encoded = "dWdnYyUzQSUyRiUyRnJpeW0lN0JoZXlfZnJyemZfZWJnZ3JhX2p2Z3VfNjQlN0RwZ3MucGJ6";

int base64(char* str){
  char table[65] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
  unsigned int len = strlen(str);

  char *new_buf = malloc(4 * len / 3 + 1);
  memset(new_buf,0, 4*(len/3)+1);

  char *p = new_buf;
  int i;

  for ( i = 0; i < len - len % 3; i += 3 ) {
    unsigned int q = (str[i] << 16) + (str[i + 1] << 8) + str[i + 2];
    p[0] = table[(q >> 18) & 0x3F];
    p[1] = table[(q >> 12) & 0x3F];
    p[2] = table[(q >> 6)  & 0x3F];
    p[3] = table[str[i + 2] & 0x3F];
    p += 4;
  }
  if ( len % 3 == 1 ) {
    p[0] = table[((unsigned int)(str[i] << 16) >> 18) & 0x3F];
    p[1] = table[16 * str[i] & 0x3F];
    p[2] = '=';
    p[3] = '=';
    p += 4;
  }
  else if ( len % 3 == 2 ) {
    unsigned int q = (str[i] << 16) + (str[i + 1] << 8);
    p[0] = table[(q >> 18) & 0x3F];
    p[1] = table[(q >> 12) & 0x3F];
    p[2] = table[(q >> 6) & 0x3F];
    p[3] = '=';
    p += 4;
  }
  *p = 0;
  return new_buf;
}

void encode(char *t, char *enc, char *tb){
	for (; *t; t++) {
		if (tb[*t]) sprintf(enc, "%c", tb[*t]);
		else        sprintf(enc, "%%%02X", *t);
		while (*++enc);
	}
}

int urlencode(char *url) {
	char *enc = malloc((strlen(url) * 3) + 1);
	memset(enc,0,(strlen(url) * 3) + 1);
 	int i;
	for (i = 0; i < 256; i++) {
		rfc3986[i] = isalnum(i)||i == '~'||i == '-'||i == '.'||i == '_'? i : 0;
		html5[i] = isalnum(i)||i == '*'||i == '-'||i == '.'||i == '_'? i : (i == ' ') ? '+' : 0;
	}
 	encode(url, enc, rfc3986);
	return enc;
}

int rot13(const char *str) {
  char *s = (char *)str;
  char *new_str = malloc(strlen(str) + 1);
  char *p = new_str;
  while ( *s ) {
    if ( *s <= '@' || *s > 'Z' ) {
      if ( *s <= '`' || *s > 'z' )
        *p = *s;
      else
        *p = (*s - 'T') % 26 + 'a';
    }
    else {
      *p = (*s - '4') % 26 + 'A';
    }
    ++p;
    ++s;
  }
  *p = 0;
  return new_str;
}

int main(int argc, char **argv) {
 if ( argc != 2 ) {
    puts("./findme <<key>> ");
    exit(0);
  }
  char *input = (char *)malloc(strlen(argv[1]) + 1); //safekeeping :)
  memset(input,0,strlen(argv[1]) + 1);
  strncpy(input, argv[1], strlen(argv[1])); // oof safekeeping 2 :)

  char *flag = base64(urlencode(rot13(input)));
  if ( !strcmp(flag, flag_encoded) )
    puts("GG!, now put that flag on ye head and fly away!!");
  else
    puts("Nope, wrong flag ye got there m8, try again!");
  return 0;
}
