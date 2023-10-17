#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <sys/time.h>
#include <unistd.h>

double distancia;


// Función que genera el código HTML para visualizar coordenadas en un mapa de Google
void generarCodigoHTML(float coordenadas[][2], int numCoordenadas, const char* apiKey) {


	float X = (coordenadas[0][0] + coordenadas[numCoordenadas - 1][0]) / 2;
	float Y = (coordenadas[0][1] + coordenadas[numCoordenadas - 1][1]) / 2;

    printf("<!DOCTYPE html>\n");
    printf("<html>\n");
    printf("  <head>\n");
    printf("    <title>Mapa con Coordenadas</title>\n");
    printf("    <script src=\"https://maps.googleapis.com/maps/api/js?key=%s\"></script>\n", apiKey);
    printf("  </head>\n");
    printf("  <body>\n");
    printf("    <div id=\"map\" style=\"height: 800px; width: 100%%;\"></div>\n");
    printf("    <script>\n");
    printf("      function initMap() {\n");
    printf("        var map = new google.maps.Map(document.getElementById(\"map\"), {\n");
    printf("          zoom: 18,\n");
    printf("          center: { lat: %.6f, lng: %.6f },\n",X,Y);
    printf("          mapTypeId: google.maps.MapTypeId.SATELLITE\n");
    printf("        });\n");

    // Recorrer las coordenadas y agregar marcadores
    for (int i = 0; i < numCoordenadas; i++) {
        printf("        new google.maps.Marker({\n");
        printf("          position: { lat: %.6f, lng: %.6f },\n", coordenadas[i][0], coordenadas[i][1]);
        printf("          map: map,\n");
        if (i==0) {
			printf("          label: \"Mtr\"\n");
        }else{
			if (i!=(numCoordenadas-1)) printf("          label: \"%d\"\n", i);
			else printf("          label: \"Obj\"\n");
		}
        //printf("          icon: \"http://maps.google.com/mapfiles/ms/micons/blue.png\"\n");
        printf("        });\n");
    }


// Agregar una línea con forma de flecha entre el primer y último punto con texto en el centro
    printf("        var linea = new google.maps.Polyline({\n");
    printf("          path: [\n");
    printf("            { lat: %.6f, lng: %.6f },\n", coordenadas[0][0], coordenadas[0][1]); // Primer punto
    printf("            { lat: %.6f, lng: %.6f }  // Último punto\n", coordenadas[numCoordenadas - 1][0], coordenadas[numCoordenadas - 1][1]);
    printf("          ],\n");
    printf("          geodesic: true,\n");
    printf("          icons: [{\n");
    printf("            icon: { path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW },\n");
    printf("            offset: '100',\n");
    printf("          }],\n");
    printf("          strokeColor: '#FF0000', // Color de la línea (rojo)\n");
    printf("          strokeOpacity: 1.0, // Opacidad de la línea (1.0 es completamente opaco)\n");
    printf("          strokeWeight: 2 // Grosor de la línea\n");
    printf("        });\n");


    printf("        linea.setMap(map);\n"); // Agregar la línea al mapa

 // Crear un texto en el centro de la línea
    printf("        var centerLatLng = new google.maps.LatLng(%.6f, %.6f); \n",X,Y);
    printf("        var textoEnCentro = new google.maps.InfoWindow({\n");
    printf("          content: '%.2f m',\n",distancia);
    printf("        });\n");
    printf("        textoEnCentro.setPosition(centerLatLng);\n");
    printf("        textoEnCentro.open(map);\n");



    printf("      }\n");
    printf("    </script>\n");
    printf("    <script>\n");
    printf("      initMap();\n");
    printf("    </script>\n");
    printf("  </body>\n");
    printf("</html>\n");
}


void L2G(double decimal, int *grados, int *minutos, double *segundos) {
    // Verificar si el valor es negativo
    int signo = (decimal < 0) ? -1 : 1;
    decimal = fabs(decimal);

    // Calcular los grados
    *grados = (int)decimal;

    // Calcular los minutos
    double minutosDecimales = (decimal - *grados) * 60;
    *minutos = (int)minutosDecimales;

    // Calcular los segundos
    *segundos = (minutosDecimales - *minutos) * 60;

    // Aplicar el signo correcto
    *grados *= signo;
}

float addwobble(float valorInicial, float porcentajeMaximo) {

    // Generar un número aleatorio entre -1 y 1
    float signoAleatorio = ((float)rand() / RAND_MAX) * 2 - 1;

    // Calcular el valor aleatorio dentro del rango
    float valorAleatorio = signoAleatorio * porcentajeMaximo * valorInicial;

    // Calcular el valor final
    float valorFinal = valorInicial + valorAleatorio;

    return valorFinal;
}

int gA, mA, gO, mO;
double sA, sO;





// Función para calcular la distancia recorrida por un proyectil en una trayectoria parabólica
double calcularDistanciaProyectil(double angulo, double velocidadInicial) {
    const double gravedad = 9.81; // Asumimos una aceleración debida a la gravedad de 9.81 m/s^2

    // Convertir el ángulo de grados a radianes
    double anguloRadianes = angulo * M_PI / 180.0;

    // Calcular la distancia
    double distancia = (velocidadInicial * velocidadInicial * sin(2 * anguloRadianes)) / gravedad;

    return distancia;
}

// Función para calcular las coordenadas de impacto
void calcularCoordenadasImpacto(double latitudInicial, double longitudInicial, double direccion, double distancia, double *latitudImpacto, double *longitudImpacto) {
    // Radio de la Tierra en metros
    const double radioTierra = 6371000.0;

    // Convertir la dirección en grados a radianes
    double direccionRadianes = direccion * M_PI / 180.0;

    // Convertir latitud y longitud inicial a radianes
    double latitudRadianes = latitudInicial * M_PI / 180.0;
    double longitudRadianes = longitudInicial * M_PI / 180.0;

    // Calcular las coordenadas cartesianas del impacto
    double xImpacto = distancia * cos(direccionRadianes);
    double yImpacto = distancia * sin(direccionRadianes);

    // Calcular las coordenadas esféricas del impacto
    double nuevaLatitudRadianes = asin(sin(latitudRadianes) * cos(distancia / radioTierra) + cos(latitudRadianes) * sin(distancia / radioTierra) * cos(direccionRadianes));
    double nuevaLongitudRadianes = longitudRadianes + atan2(sin(direccionRadianes) * sin(distancia / radioTierra) * cos(latitudRadianes), cos(distancia / radioTierra) - sin(latitudRadianes) * sin(nuevaLatitudRadianes));

    // Convertir las coordenadas esféricas del impacto a grados
    *latitudImpacto = nuevaLatitudRadianes * 180.0 / M_PI;
    *longitudImpacto = nuevaLongitudRadianes * 180.0 / M_PI;
}


int main(int argc, char *argv[]) {

	// Obtener la marca de tiempo actual en milisegundos
    struct timeval tiempo;
    gettimeofday(&tiempo, NULL);
    unsigned long semilla = tiempo.tv_sec * 1000 + tiempo.tv_usec / 1000;

    srand((unsigned)semilla*(unsigned long)getpid());



    double velocidadInicial=90;

    if (argc != 7) {
        printf("Uso: %s <Lat> <Long> <disparos> <azimut> <direccion> <dispersion>\n", argv[0]);
        return 1;
    }
    double latitudInicial = atof(argv[1]);
    double longitudInicial = atof(argv[2]);
	int N = atoi(argv[3]);
    double angulo = atof(argv[4]);
    double direccion = atof(argv[5]);
	float dispersion = atof(argv[6]);;

    distancia = calcularDistanciaProyectil(angulo, velocidadInicial);
    double latitudImpacto, longitudImpacto;
    calcularCoordenadasImpacto(latitudInicial, longitudInicial, direccion, distancia, &latitudImpacto, &longitudImpacto);


 /*
    L2G(latitudImpacto, &gA, &mA, &sA);
    L2G(longitudImpacto, &gO, &mO, &sO);
    printf("impacto:\n%d %d %.2lf ; %d %d %.2lf\n", gA, mA, sA, gO, mO, sO);
    printf("Distancia: %.2lf m\n", distancia);
*/

    // Tu clave de API de Google Maps
    const char* apiKey = "AIzaSyA5FuC-FpZNRVKEl2ZxzEm4DLoC9Mkgg3Y";

    // Definir un vector de coordenadas (latitud, longitud)
    float coordenadas[N+2][2];

	//guardo punto de disparo
	coordenadas[0][0] = latitudInicial;
	coordenadas[0][1] = longitudInicial;

	//printf("calculando impactos");
    // Ingresar las coordenadas
    for (int i = 1; i < N+1; i++) {
		coordenadas[i][0] = addwobble(latitudImpacto,dispersion/10000000);
		coordenadas[i][1] = addwobble(longitudImpacto,dispersion/10000000);
    }

	//guardo centro de impacto
	coordenadas[N+1][0] = latitudImpacto;
	coordenadas[N+1][1] = longitudImpacto;



    // Llamar a la función para generar el código HTML
    generarCodigoHTML(coordenadas, N+2, apiKey);



    return 0;
}



