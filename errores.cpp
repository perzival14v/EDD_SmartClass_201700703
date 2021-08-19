#include "errores.h"
#include <string.h>
#include <string>
#include <stdio.h>
#include <ctype.h>


using namespace std;

errores::errores(){
	id=-1;
	tipo="vacio";
	descripcion="vacio";
}


errores::errores(int _id,string _tipo,string _descripcion)
{
	id=_id;
	tipo=_tipo;
	descripcion=_descripcion;
	
}
