
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     PROGRAM = 258,
     LIST = 259,
     WHILE = 260,
     INT = 261,
     STRING = 262,
     CHAR = 263,
     IF = 264,
     ELSE = 265,
     FINISH = 266,
     plus = 267,
     minus = 268,
     multiply = 269,
     divide = 270,
     modulo = 271,
     lessOrEqual = 272,
     moreOrEqual = 273,
     less = 274,
     more = 275,
     equal = 276,
     assign = 277,
     leftCurlyBracket = 278,
     rightCurlyBracket = 279,
     leftRoundBracket = 280,
     rightRoundBracket = 281,
     leftBracket = 282,
     rightBracket = 283,
     semicolon = 284,
     comma = 285,
     colon = 286,
     apostrophe = 287,
     quote = 288,
     identifier = 289,
     integer_constant = 290,
     char_constant = 291,
     string_constant = 292
   };
#endif
/* Tokens.  */
#define PROGRAM 258
#define LIST 259
#define WHILE 260
#define INT 261
#define STRING 262
#define CHAR 263
#define IF 264
#define ELSE 265
#define FINISH 266
#define plus 267
#define minus 268
#define multiply 269
#define divide 270
#define modulo 271
#define lessOrEqual 272
#define moreOrEqual 273
#define less 274
#define more 275
#define equal 276
#define assign 277
#define leftCurlyBracket 278
#define rightCurlyBracket 279
#define leftRoundBracket 280
#define rightRoundBracket 281
#define leftBracket 282
#define rightBracket 283
#define semicolon 284
#define comma 285
#define colon 286
#define apostrophe 287
#define quote 288
#define identifier 289
#define integer_constant 290
#define char_constant 291
#define string_constant 292




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


