%If (HAS_QT3)
typedef unsigned int    GLenum;
%End // (HAS_QT3)
typedef unsigned char   GLboolean;
typedef unsigned int    GLbitfield;
typedef void            GLvoid;
typedef /*signed*/ char GLbyte;         /* 1-byte signed */
typedef short           GLshort;        /* 2-byte signed */
%If (HAS_QT3)
typedef int             GLint;          /* 4-byte signed */
%End // (HAS_QT3)
typedef unsigned char   GLubyte;        /* 1-byte unsigned */
typedef unsigned short  GLushort;       /* 2-byte unsigned */
%If (HAS_QT3)
typedef unsigned int    GLuint;         /* 4-byte unsigned */
%End // (HAS_QT3)
typedef int             GLsizei;        /* 4-byte signed */
typedef float           GLfloat;        /* single precision float */
typedef float           GLclampf;       /* single precision float in [0,1] */
typedef double          GLdouble;       /* double precision float */
typedef double          GLclampd;       /* double precision float in [0,1] */

typedef unsigned int    size_type;

// Local Variables:
// mode: C++
// c-file-style: "stroustrup"
// indent-tabs-mode: nil
// End:
