class Clasificacion:

    _equipo: str
    _partidosJugados: int
    _partidosGanados: int
    _partidosPerdidos: int
    _puntosFavor: int
    _puntosContra: int
    _puntosDiferencial: int

    def setDatos(self, clasificacion: list):
        self._equipo = clasificacion[0]
        self._partidosJugados = clasificacion[1]
        self._partidosGanados = clasificacion[2]
        self._partidosPerdidos = clasificacion[3]
        self._puntosFavor = clasificacion[4]
        self._puntosContra = clasificacion[5]
        self._puntosDiferencial = clasificacion[6]

    def getEquipo(self):
        return self._equipo
    
    def getPartidosJugados(self):
        return self._partidosJugados
    
    def getPartidosGanados(self):
        return self._partidosGanados
    
    def getPartidosPerdidos(self):
        return self._partidosPerdidos
    
    def getPuntosFavor(self):
        return self._puntosFavor
    
    def getPuntosContra(self):
        return self._puntosContra
    
    def getPuntosDiferencial(self):
        return self._puntosDiferencial
    
    def setEquipo(self, equipo):
        self._equipo = equipo
    
    def setPartidosJugados(self, partidosJugados):
        self._partidosJugados = partidosJugados
    
    def setPartidosGanados(self, partidosGanados):
        self._partidosGanados = partidosGanados
    
    def setPartidosPerdidos(self, partidosPerdidos):
        self._partidosPerdidos = partidosPerdidos
    
    def setPuntosFavor(self, puntosFavor):
        self._puntosFavor = puntosFavor
    
    def setPuntosContra(self, puntosContra):
        self._puntosContra = puntosContra
    
    def _actualizarDiferencial(self, puntosDiferencial):
        self._puntosDiferencial = puntosDiferencial


class AvanzadaEquipo:

    _equipo: str
    _partidosJugados: int
    _minutos: float
    _ritmo: float
    _eficienciaOfensiva: float
    _eficienciaDefensiva: float
    _eficienciaNeta: float
    _diferenciaPuntos: float
    _porcentajeReboteDefensivos: int
    _porcentajeReboteOfensivos: int
    _porcentajeReboteTotal: int
    _asistenciaPorPerdida: float
    _porcentajeAsistencias: int
    _porcentajeTapones: int
    _porcentajeTiroReal: int
    _eficienciaTiro: float
    _eficienciaTiroRival: float

    def setDatos(self, avanzadaEquipo: list):
        self._equipo = avanzadaEquipo[0]
        self._partidosJugados = avanzadaEquipo[1]
        self._minutos = avanzadaEquipo[2]
        self._ritmo = avanzadaEquipo[3]
        self._eficienciaOfensiva = avanzadaEquipo[4]
        self._eficienciaDefensiva = avanzadaEquipo[5]
        self._eficienciaNeta = avanzadaEquipo[6]
        self._diferenciaPuntos = avanzadaEquipo[7]
        self._porcentajeReboteDefensivos = avanzadaEquipo[8]
        self._porcentajeReboteOfensivos = avanzadaEquipo[9]
        self._porcentajeReboteTotal = avanzadaEquipo[10]
        self._asistenciaPorPerdida = avanzadaEquipo[11]
        self._porcentajeAsistencias = avanzadaEquipo[12]
        self._porcentajeTapones = avanzadaEquipo[13]
        self._porcentajeTiroReal = avanzadaEquipo[14]
        self._eficienciaTiro = avanzadaEquipo[15]
        self._eficienciaTiroRival = avanzadaEquipo[16]

    def getEquipo(self):
        return self._equipo

    def getPartidosJugados(self):
        return self._partidosJugados
    
    def getMinutos(self):
        return self._minutos
    
    def getRitmo(self):
        return self._ritmo
    
    def getEficienciaOfensiva(self):
        return self._eficienciaOfensiva
    
    def getEficienciaDefensiva(self):
        return self._eficienciaDefensiva
    
    def getEficienciaNeta(self):
        return self._eficienciaNeta
    
    def getDiferenciaPuntos(self):
        return self._diferenciaPuntos
    
    def getPorcentajeReboteDefensivos(self):
        return self._porcentajeReboteDefensivos
    
    def getPorcentajeReboteOfensivos(self):
        return self._porcentajeReboteOfensivos
    
    def getPorcentajeReboteTotal(self):
        return self._porcentajeReboteTotal
    
    def getAsistenciaPorPerdida(self):
        return self._asistenciaPorPerdida
    
    def getPorcentajeAsistencias(self):
        return self._porcentajeAsistencias
    
    def getPorcentajeTapones(self):
        return self._porcentajeTapones
    
    def getPorcentajeTiroReal(self):
        return self._porcentajeTiroReal
    
    def getEficienciaTiro(self):
        return self._eficienciaTiro
    
    def getEficienciaTiroRival(self):
        return self._eficienciaTiroRival

    def setEquipo(self, equipo):
        self._equipo = equipo

    def setPartidosJugados(self, partidosJugados):
        self._partidosJugados = partidosJugados

    def setMinutos(self, minutos):
        self._minutos = minutos

    def setRitmo(self, ritmo):
        self._ritmo = ritmo

    def setEficienciaOfensiva(self, eficienciaOfensiva):
        self._eficienciaOfensiva = eficienciaOfensiva

    def setEficienciaDefensiva(self, eficienciaDefensiva):
        self._eficienciaDefensiva = eficienciaDefensiva

    def setEficienciaNeta(self, eficienciaNeta):
        self._eficienciaNeta = eficienciaNeta

    def setDiferenciaPuntos(self, diferenciaPuntos):
        self._diferenciaPuntos = diferenciaPuntos

    def setPorcentajeReboteDefensivos(self, porcentajeReboteDefensivos):
        self._porcentajeReboteDefensivos = porcentajeReboteDefensivos

    def setPorcentajeReboteOfensivos(self, porcentajeReboteOfensivos):
        self._porcentajeReboteOfensivos = porcentajeReboteOfensivos

    def setPorcentajeReboteTotal(self, porcentajeReboteTotal):
        self._porcentajeReboteTotal = porcentajeReboteTotal

    def setAsistenciaPorPerdida(self, asistenciaPorPerdida):
        self._asistenciaPorPerdida = asistenciaPorPerdida

    def setPorcentajeAsistencias(self, porcentajeAsistencias):
        self._porcentajeAsistencias = porcentajeAsistencias

    def setPorcentajeTapones(self, porcentajeTapones):
        self._porcentajeTapones = porcentajeTapones

    def setPorcentajeTiroReal(self, porcentajeTiroReal):
        self._porcentajeTiroReal = porcentajeTiroReal

    def setEficienciaTiro(self, eficienciaTiro):
        self._eficienciaTiro = eficienciaTiro

    def setEficienciaTiroRival(self, eficienciaTiroRival):
        self._eficienciaTiroRival = eficienciaTiroRival


class AvanzadaJugador:

    _jug: str
    _jugador: str
    _equipo: str
    _partidosJugados: int
    _minutos: int
    _ritmo: int
    _porcentajePosesiones: int
    _porcentajePosesionesLanzados: int
    _eficienciaOfensiva: int
    _eficienciaDefensiva: int
    _eficienciaNeta: int
    _influencia: int
    _porcentajeReboteDefensiva: int
    _porcentajeReboteOfensiva: int
    _porcentajeReboteTotal: int
    _asistenciaPorPerdida: int
    _porcentajeAsistencias: int
    _porcentajeTapones: int
    _porcentajeTiroReal: int
    _eficienciaTiro: int
    _eficienciaTiroRival: int

    def setDatos(self, avanzadaJugador: list):
        self._jug = avanzadaJugador[0]
        self._jugador = avanzadaJugador[1]
        self._equipo = avanzadaJugador[2]
        self._partidosJugados = avanzadaJugador[3]
        self._minutos = avanzadaJugador[4]
        self._ritmo = avanzadaJugador[5]
        self._porcentajePosesiones = avanzadaJugador[6]
        self._porcentajePosesionesLanzados = avanzadaJugador[7]
        self._eficienciaOfensiva = avanzadaJugador[8]
        self._eficienciaDefensiva = avanzadaJugador[9]
        self._eficienciaNeta = avanzadaJugador[10]
        self._influencia = avanzadaJugador[11]
        self._porcentajeReboteDefensiva = avanzadaJugador[12]
        self._porcentajeReboteOfensiva = avanzadaJugador[13]
        self._porcentajeReboteTotal = avanzadaJugador[14]
        self._asistenciaPorPerdida = avanzadaJugador[15]
        self._porcentajeAsistencias = avanzadaJugador[16]
        self._porcentajeTapones = avanzadaJugador[17]
        self._porcentajeTiroReal = avanzadaJugador[18]
        self._eficienciaTiro = avanzadaJugador[19]
        self._eficienciaTiroRival = avanzadaJugador[20]

    def setJug(self, jug):
        self._jug = jug

    def getJug(self):
        return self._jug

    def setJugador(self, jugador):
        self._jugador = jugador        

    def getJugador(self):
        return self._jugador

    def setEquipo(self, equipo):
        self._equipo = equipo
        
    def getEquipo(self):
        return self._equipo
    
    def setPartidosJugados(self, partidosJugados):
        self._partidosJugados = partidosJugados

    def getPartidosJugados(self):
        return self._partidosJugados

    def setMinutos(self, minutos):
        self._minutos = minutos

    def getMinutos(self):
        return self._minutos

    def setRitmo(self, ritmo):
        self._ritmo = ritmo

    def getRitmo(self):
        return self._ritmo

    def setPorcentajePosesiones(self, porcentajePosesiones):
        self._porcentajePosesiones = porcentajePosesiones

    def getPorcentajePosesiones(self):
        return self._porcentajePosesiones

    def setPorcentajePosesionesLanzados(self, porcentajePosesionesLanzados):
        self._porcentajePosesionesLanzados = porcentajePosesionesLanzados

    def getPorcentajePosesionesLanzados(self):
        return self._porcentajePosesionesLanzados

    def setEficienciaOfensiva(self, eficienciaOfensiva):
        self._eficienciaOfensiva = eficienciaOfensiva

    def getEficienciaOfensiva(self):
        return self._eficienciaOfensiva

    def setEficienciaDefensiva(self, eficienciaDefensiva):
        self._eficienciaDefensiva = eficienciaDefensiva

    def getEficienciaDefensiva(self):
        return self._eficienciaDefensiva

    def setEficienciaNeta(self, eficienciaNeta):
        self._eficienciaNeta = eficienciaNeta

    def getEficienciaNeta(self):
        return self._eficienciaNeta
    
    def setInfluencia(self, influencia):
        self._influencia = influencia

    def getInfluencia(self):
        return self._influencia
    
    def setPorcentajeReboteDefensiva(self, porcentajeReboteDefensiva):
        self._porcentajeReboteDefensiva = porcentajeReboteDefensiva

    def getPorcentajeReboteDefensiva(self):
        return self._porcentajeReboteDefensiva

    def setPorcentajeReboteOfensiva(self, porcentajeReboteOfensiva):
        self._porcentajeReboteOfensiva = porcentajeReboteOfensiva

    def getPorcentajeReboteOfensiva(self):
        return self._porcentajeReboteOfensiva
    
    def setPorcentajeReboteTotal(self, porcentajeReboteTotal):
        self._porcentajeReboteTotal = porcentajeReboteTotal

    def getPorcentajeReboteTotal(self):
        return self._porcentajeReboteTotal
    
    def setAsistenciaPorPerdida(self, asistenciaPorPerdida):
        self._asistenciaPorPerdida = asistenciaPorPerdida

    def getAsistenciaPorPerdida(self):
        return self._asistenciaPorPerdida
    
    def setPorcentajeAsistencias(self, porcentajeAsistencias):
        self._porcentajeAsistencias = porcentajeAsistencias

    def getPorcentajeAsistencias(self):
        return self._porcentajeAsistencias

    def setPorcentajeTapones(self, porcentajeTapones):
        self._porcentajeTapones = porcentajeTapones

    def getPorcentajeTapones(self):
        return self._porcentajeTapones
    
    def setPorcentajeTiroReal(self, porcentajeTiroReal):
        self._porcentajeTiroReal = porcentajeTiroReal

    def getPorcentajeTiroReal(self):
        return self._porcentajeTiroReal

    def setEficienciaTiro(self, eficienciaTiro):
        self._eficienciaTiro = eficienciaTiro

    def getEficienciaTiro(self):
        return self._eficienciaTiro
    
    def setEficienciaTiroRival(self, eficienciaTiroRival):
        self._eficienciaTiroRival = eficienciaTiroRival

    def getEficienciaTiroRival(self):
        return self._eficienciaTiroRival
    

class TirosJugador:

    _jug: str
    _jugador: str
    _equipo: str
    _tirosLibresAnotados: int
    _tirosLibresLanzados: int
    _porcentajeTirosLibres: float
    _tiros2Anotados: int
    _tiros2Lanzados: int
    _porcentajeTiros2: float
    _tiros3Anotados: int
    _tiros3Lanzados: int
    _porcentajeTiros3: float

    def setDatos(self, tirosJugador: list):
        self._jug = tirosJugador[0]
        self._jugador = tirosJugador[1]
        self._equipo = tirosJugador[2]
        self._tirosLibresAnotados = tirosJugador[3]
        self._tirosLibresLanzados = tirosJugador[4]
        self._porcentajeTirosLibres = tirosJugador[5]
        self._tiros2Anotados = tirosJugador[6]
        self._tiros2Lanzados = tirosJugador[7]
        self._porcentajeTiros2 = tirosJugador[8]
        self._tiros3Anotados = tirosJugador[9]
        self._tiros3Lanzados = tirosJugador[10]
        self._porcentajeTiros3 = tirosJugador[11]
    
    def setJug(self, jug):
        self._jug = jug

    def getJug(self):
        return self._jug

    def setJugador(self, jugador):
        self._jugador = jugador
    
    def getJugador(self):
        return self._jugador

    def setEquipo(self, equipo):
        self._equipo = equipo
    
    def getEquipo(self):
        return self._equipo

    def setTirosLibresAnotados(self, tirosLibresAnotados):
        self._tirosLibresAnotados = tirosLibresAnotados

    def getTirosLibresAnotados(self):
        return self._tirosLibresAnotados

    def setTirosLibresLanzados(self, tirosLibresLanzados):
        self._tirosLibresLanzados = tirosLibresLanzados

    def getTirosLibresLanzados(self):
        return self._tirosLibresLanzados

    def setPorcentajeTirosLibres(self, porcentajeTirosLibres):
        self._porcentajeTirosLibres = porcentajeTirosLibres

    def getPorcentajeTirosLibres(self):
        return self._porcentajeTirosLibres

    def setTiros2Anotados(self, tiros2Anotados):
        self._tiros2Anotados = tiros2Anotados

    def getTiros2Anotados(self):
        return self._tiros2Anotados

    def setTiros2Lanzados(self, tiros2Lanzados):
        self._tiros2Lanzados = tiros2Lanzados

    def getTiros2Lanzados(self):
        return self._tiros2Lanzados

    def setPorcentajeTiros2(self, porcentajeTiros2):
        self._porcentajeTiros2 = porcentajeTiros2

    def getPorcentajeTiros2(self):
        return self._porcentajeTiros2

    def setTiros3Anotados(self, tiros3Anotados):
        self._tiros3Anotados = tiros3Anotados

    def getTiros3Anotados(self):
        return self._tiros3Anotados

    def setTiros3Lanzados(self, tiros3Lanzados):
        self._tiros3Lanzados = tiros3Lanzados

    def getTiros3Lanzados(self):
        return self._tiros3Lanzados

    def setPorcentajeTiros3(self, porcentajeTiros3):
        self._porcentajeTiros3 = porcentajeTiros3

    def getPorcentajeTiros3(self):
        return self._porcentajeTiros3


class TirosEquipo:

    _equipo: str
    _tirosLibresAnotados: int
    _tirosLibresLanzados: int
    _porcentajeTirosLibres: float
    _tiros2Anotados: int
    _tiros2Lanzados: int
    _porcentajeTiros2: float
    _tiros3Anotados: int
    _tiros3Lanzados: int
    _porcentajeTiros3: float

    def setDatos(self, tirosEquipo: list):
        self._equipo = tirosEquipo[0]
        self._tirosLibresAnotados = tirosEquipo[1]
        self._tirosLibresLanzados = tirosEquipo[2]
        self._porcentajeTirosLibres = tirosEquipo[3]
        self._tiros2Anotados = tirosEquipo[4]
        self._tiros2Lanzados = tirosEquipo[5]
        self._porcentajeTiros2 = tirosEquipo[6]
        self._tiros3Anotados = tirosEquipo[7]
        self._tiros3Lanzados = tirosEquipo[8]
        self._porcentajeTiros3 = tirosEquipo[9]

    def setEquipo(self, equipo):
        self._equipo = equipo
    
    def getEquipo(self):
        return self._equipo

    def setTirosLibresAnotados(self, tirosLibresAnotados):
        self._tirosLibresAnotados = tirosLibresAnotados

    def getTirosLibresAnotados(self):
        return self._tirosLibresAnotados

    def setTirosLibresLanzados(self, tirosLibresLanzados):
        self._tirosLibresLanzados = tirosLibresLanzados

    def getTirosLibresLanzados(self):
        return self._tirosLibresLanzados

    def setPorcentajeTirosLibres(self, porcentajeTirosLibres):
        self._porcentajeTirosLibres = porcentajeTirosLibres

    def getPorcentajeTirosLibres(self):
        return self._porcentajeTirosLibres

    def setTiros2Anotados(self, tiros2Anotados):
        self._tiros2Anotados = tiros2Anotados

    def getTiros2Anotados(self):
        return self._tiros2Anotados

    def setTiros2Lanzados(self, tiros2Lanzados):
        self._tiros2Lanzados = tiros2Lanzados

    def getTiros2Lanzados(self):
        return self._tiros2Lanzados

    def setPorcentajeTiros2(self, porcentajeTiros2):
        self._porcentajeTiros2 = porcentajeTiros2

    def getPorcentajeTiros2(self):
        return self._porcentajeTiros2

    def setTiros3Anotados(self, tiros3Anotados):
        self._tiros3Anotados = tiros3Anotados

    def getTiros3Anotados(self):
        return self._tiros3Anotados

    def setTiros3Lanzados(self, tiros3Lanzados):
        self._tiros3Lanzados = tiros3Lanzados

    def getTiros3Lanzados(self):
        return self._tiros3Lanzados

    def setPorcentajeTiros3(self, porcentajeTiros3):
        self._porcentajeTiros3 = porcentajeTiros3

    def getPorcentajeTiros3(self):
        return self._porcentajeTiros3


class InfluenciaBaja:

    _jugador: str
    _minutosSinEl: float
    _minutosConEl: float
    _minutosDiferencial: float
    _anotacionSinEl: float
    _anotacionConEl: float
    _anotacionDiferencial: float
    _valoracionSinEl: float
    _valoracionConEl: float
    _valoracionDiferencial: float

    def setDatos(self, influenciaBaja: list):
        self._jugador = influenciaBaja[0]
        self._minutosSinEl= influenciaBaja[1]
        self._minutosConEl = influenciaBaja[2]
        self._minutosDiferencial = influenciaBaja[3]
        self._anotacionSinEl = influenciaBaja[4]
        self._anotacionConEl = influenciaBaja[5]
        self._anotacionDiferencial = influenciaBaja[6]
        self._valoracionSinEl = influenciaBaja[7]
        self._valoracionConEl = influenciaBaja[8]
        self._valoracionDiferencial = influenciaBaja[9]

    def setJugador(self, jugador):
        self._jugador = jugador

    def getJugador(self):
        return  self._jugador

    def setMinutosSinEl(self, minutosSinEl):
        self._minutosSinEl = minutosSinEl

    def getMinutosSinEl(self):
        return self._minutosSinEl

    def setMinutosConEl(self, minutosConEl):
        self._minutosConEl = minutosConEl

    def getMinutosConEl(self):
        return self._minutosConEl

    def setMinutosDiferencial(self, minutosDiferencial):
        self._minutosDiferencial = minutosDiferencial

    def getMinutosDiferencial(self):
        return self._minutosDiferencial

    def setAnotacionSinEl(self, anotacionesSinEl):
        self._anotacionSinEl = anotacionesSinEl
    
    def getAnotacionSinEl(self):
        return self._anotacionSinEl

    def setAnotacionConEl(self, anotacionesConEl):
        self._anotacionConEl = anotacionesConEl

    def getAnotacionConEl(self):
        return self._anotacionConEl

    def setAnotacionDiferencial(self, anotacionDiferencial):
        self._anotacionDiferencial = anotacionDiferencial

    def getAnotacionDiferencial(self):
        return self._anotacionDiferencial

    def setValoracionSinEl(self, valoracionSinEl):
        self._valoracionSinEl = valoracionSinEl

    def getValoracionSinEl(self):
        return self._valoracionSinEl

    def setValoracionConEl(self, valoracionConEl):
        self._valoracionConEl = valoracionConEl
    
    def getValoracionConEl(self):
        return self._valoracionConEl

    def setValoracionDiferencial(self, valoracionDiferencial):
        self._valoracionDiferencial = valoracionDiferencial

    def getValoracionDiferencial(self):    
        return self._valoracionDiferencial




