import CallFarmaDao
import DrogariaCristal
import DrogariaNetDao
import DrogariaPerequeDao
import DrogariaSaoPaulo
import DrogasRaiaDao
import OnofreDao
import PachecoDao
import PagueMenosDao
import UltraFarmaDao
import VenancioDao


def recoverData():
    CallFarmaDao.recoverMedicineCallFarma()
    DrogariaCristal.recoverMedicineDrogariaCristal()
    DrogariaNetDao.recoverMedicineDrogariaNet()
    DrogariaPerequeDao.recoverMedicineDrogariaPereque()
    DrogariaSaoPaulo.recoverMedicineDrogariaSaoPaulo()
    DrogasRaiaDao.recoverMedicineDrogasRaia()
    OnofreDao.recoverMedicineOnofre()
    PachecoDao.recoverMedicinePacheco()
    PagueMenosDao.recoverMedicinePagueMenos()
    UltraFarmaDao.recoverMedicineUltraFarma()
    VenancioDao.recoverMedicineVenancio()