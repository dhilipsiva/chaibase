# flake8: noqa

from peewee import *

database = SqliteDatabase('dbs/db.sqlite3', **{})

class BaseModel(Model):
    class Meta:
        database = database

class Config(BaseModel):
    mroundoff = IntegerField(db_column='mRoundoff', null=True)
    mleafweighing = IntegerField(null=True)

    class Meta:
        db_table = 'Config'
        primary_key = False

class Deductiondetails(BaseModel):
    mdeductweight = IntegerField(db_column='mDeductWeight', null=True)
    mdeductiontype = TextField(db_column='mDeductionType', null=True)  # varchar
    mdeductioncode = IntegerField(db_column='mDeductioncode', null=True)
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)

    class Meta:
        db_table = 'DeductionDetails'
        primary_key = False

class Deductionmst(BaseModel):
    mdeductioncode = IntegerField(db_column='mDeductionCode', null=True)
    mdeductiontype = TextField(db_column='mDeductionType', null=True)  # varchar

    class Meta:
        db_table = 'DeductionMst'
        primary_key = False

class Leafmst(BaseModel):
    mleafcode = IntegerField(db_column='mLeafCode', null=True)
    mleafname = TextField(db_column='mLeafName', null=True)  # varchar

    class Meta:
        db_table = 'LeafMst'
        primary_key = False

class Leafsupplyhdr(BaseModel):
    ma = IntegerField(db_column='mA', null=True)
    mb = IntegerField(db_column='mB', null=True)
    mbb = IntegerField(db_column='mBB', null=True)
    mbags = IntegerField(db_column='mBags', null=True)
    mc = IntegerField(db_column='mC', null=True)
    mcheckedbycode = IntegerField(db_column='mCheckedbyCode', null=True)
    mcheckedbyname = TextField(db_column='mCheckedbyName', null=True)  # varchar
    mconfirmation = IntegerField(db_column='mConfirmation', null=True)
    mconfirmedtime = DateTimeField(db_column='mConfirmedtime', null=True)
    mconfirmmdate = DateTimeField(db_column='mConfirmmDate', null=True)
    mconfirmmtime = DateTimeField(db_column='mConfirmmTime', null=True)
    mdeductionweight = IntegerField(db_column='mDeductionweight', null=True)
    mentertime = DateTimeField(db_column='mEntertime', null=True)
    mexcessweight = FloatField(db_column='mExcessWeight', null=True)
    mgrossweight = IntegerField(db_column='mGrossweight', null=True)
    mindividualname = TextField(db_column='mIndividualName', null=True)  # varchar
    mmode = TextField(db_column='mMode', null=True)  # varchar
    mnetweight = IntegerField(db_column='mNetweight', null=True)
    mprintok = IntegerField(db_column='mPrintok', null=True)
    mshedcode = IntegerField(db_column='mShedCode', null=True)
    mshedname = TextField(db_column='mShedName', null=True)  # varchar
    mshedsupplycode = IntegerField(db_column='mShedSupplyCode', null=True)
    mshedtype = IntegerField(db_column='mShedType', null=True)
    msno = IntegerField(db_column='mSno', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    msuppliername = TextField(db_column='mSupplierName', null=True)  # varchar
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)
    msupplydate = DateTimeField(db_column='mSupplydate', null=True)
    mturfname = TextField(db_column='mTurfName', null=True)  # varchar
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)
    mvehiclein = DateTimeField(db_column='mVehicleIn', null=True)
    mvehiclename = TextField(db_column='mVehicleName', null=True)  # varchar
    mvehicleout = DateTimeField(db_column='mVehicleOut', null=True)
    mweighedbycode = IntegerField(db_column='mWeighedbyCode', null=True)
    mweighedbyname = TextField(db_column='mWeighedbyName', null=True)  # varchar
    mweighedtime = DateTimeField(db_column='mWeighedtime', null=True)

    class Meta:
        db_table = 'LeafSupplyHdr'
        primary_key = False

class Leafsupplyheader(BaseModel):
    ma = IntegerField(db_column='mA', null=True)
    mb = IntegerField(db_column='mB', null=True)
    mbb = IntegerField(db_column='mBB', null=True)
    mbags = IntegerField(db_column='mBags', null=True)
    mc = IntegerField(db_column='mC', null=True)
    mcheckedbycode = IntegerField(db_column='mCheckedbyCode', null=True)
    mcheckedbyname = TextField(db_column='mCheckedbyName', null=True)  # varchar
    mconfirmation = IntegerField(db_column='mConfirmation', null=True)
    mconfirmedtime = DateTimeField(db_column='mConfirmedtime', null=True)
    mconfirmmdate = DateTimeField(db_column='mConfirmmDate', null=True)
    mconfirmmtime = DateTimeField(db_column='mConfirmmTime', null=True)
    mdeductionweight = IntegerField(db_column='mDeductionweight', null=True)
    mentertime = DateTimeField(db_column='mEntertime', null=True)
    mexcessweight = IntegerField(db_column='mExcessWeight', null=True)
    mgrossweight = IntegerField(db_column='mGrossweight', null=True)
    mindividualname = TextField(db_column='mIndividualName', null=True)  # varchar
    mmode = TextField(db_column='mMode', null=True)  # varchar
    mnetweight = IntegerField(db_column='mNetweight', null=True)
    mprintok = IntegerField(db_column='mPrintok', null=True)
    mshedcode = IntegerField(db_column='mShedCode', null=True)
    mshedname = TextField(db_column='mShedName', null=True)  # varchar
    mshedsupplycode = IntegerField(db_column='mShedSupplyCode', null=True)
    mshedtype = IntegerField(db_column='mShedType', null=True)
    msno = IntegerField(db_column='mSno', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    msuppliername = TextField(db_column='mSupplierName', null=True)  # varchar
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)
    msupplydate = DateTimeField(db_column='mSupplydate', null=True)
    mturfname = TextField(db_column='mTurfName', null=True)  # varchar
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)
    mvehiclein = DateTimeField(db_column='mVehicleIn', null=True)
    mvehiclename = TextField(db_column='mVehicleName', null=True)  # varchar
    mvehicleout = DateTimeField(db_column='mVehicleOut', null=True)
    mweighedbycode = IntegerField(db_column='mWeighedbyCode', null=True)
    mweighedbyname = TextField(db_column='mWeighedbyName', null=True)  # varchar
    mweighedtime = DateTimeField(db_column='mWeighedtime', null=True)

    class Meta:
        db_table = 'LeafSupplyHeader'
        primary_key = False

class Leafsupplyinbag(BaseModel):
    mbagserialno = IntegerField(db_column='mBagSerialNo', null=True)
    mbagweight = IntegerField(db_column='mBagWeight', null=True)
    mdate = DateTimeField(db_column='mDate', null=True)
    mexcessweight = FloatField(db_column='mExcessweight', null=True)
    mnoofbags = IntegerField(db_column='mNoofBags', null=True)
    msupplyhdrcode = IntegerField(db_column='mSupplyHdrCode', null=True)
    mtime = DateTimeField(db_column='mTime', null=True)

    class Meta:
        db_table = 'LeafSupplyInBag'
        primary_key = False

class Leaftransferdetails(BaseModel):
    mleafcode = IntegerField(db_column='mLeafCode', null=True)
    mleafname = TextField(db_column='mLeafName', null=True)  # varchar
    mleafweight = IntegerField(db_column='mLeafWeight', null=True)
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)

    class Meta:
        db_table = 'LeafTransferDetails'
        primary_key = False

class Mconfig(BaseModel):
    mbitspersecond = IntegerField(db_column='mBitsPerSecond', null=True)
    mdatabits = IntegerField(db_column='mDataBits', null=True)
    menabled = IntegerField(db_column='mEnabled', null=True)
    mendtime = DateTimeField(db_column='mEndTime', null=True)
    mintervalhr = IntegerField(db_column='mIntervalHr', null=True)
    mintervalmin = IntegerField(db_column='mIntervalMin', null=True)
    mmobilenumber = FloatField(db_column='mMobileNumber', null=True)
    mparity = TextField(db_column='mParity', null=True)  # varchar
    mport = IntegerField(db_column='mPort', null=True)
    mstarttime = DateTimeField(db_column='mStartTime', null=True)
    mstopbits = IntegerField(db_column='mStopBits', null=True)

    class Meta:
        db_table = 'MConfig'
        primary_key = False

class P(BaseModel):
    mpassword = TextField(db_column='mPassword', null=True)  # varchar

    class Meta:
        db_table = 'P'
        primary_key = False

class Pasteerrors(BaseModel):
    ma = IntegerField(db_column='mA', null=True)
    mb = IntegerField(db_column='mB', null=True)
    mbb = IntegerField(db_column='mBB', null=True)
    mbags = IntegerField(db_column='mBags', null=True)
    mc = IntegerField(db_column='mC', null=True)
    mcheckedbycode = IntegerField(db_column='mCheckedbyCode', null=True)
    mcheckedbyname = TextField(db_column='mCheckedbyName', null=True)  # varchar
    mconfirmation = IntegerField(db_column='mConfirmation', null=True)
    mconfirmedtime = DateTimeField(db_column='mConfirmedtime', null=True)
    mconfirmmdate = DateTimeField(db_column='mConfirmmDate', null=True)
    mconfirmmtime = DateTimeField(db_column='mConfirmmTime', null=True)
    mdeductionweight = IntegerField(db_column='mDeductionweight', null=True)
    mentertime = DateTimeField(db_column='mEntertime', null=True)
    mexcessweight = IntegerField(db_column='mExcessWeight', null=True)
    mgrossweight = IntegerField(db_column='mGrossweight', null=True)
    mindividualname = TextField(db_column='mIndividualName', null=True)  # varchar
    mmode = TextField(db_column='mMode', null=True)  # varchar
    mnetweight = IntegerField(db_column='mNetweight', null=True)
    mprintok = IntegerField(db_column='mPrintok', null=True)
    mshedcode = IntegerField(db_column='mShedCode', null=True)
    mshedname = TextField(db_column='mShedName', null=True)  # varchar
    mshedsupplycode = IntegerField(db_column='mShedSupplyCode', null=True)
    mshedtype = IntegerField(db_column='mShedType', null=True)
    msno = IntegerField(db_column='mSno', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    msuppliername = TextField(db_column='mSupplierName', null=True)  # varchar
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)
    msupplydate = DateTimeField(db_column='mSupplydate', null=True)
    mturfname = TextField(db_column='mTurfName', null=True)  # varchar
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)
    mvehiclename = TextField(db_column='mVehicleName', null=True)  # varchar
    mweighedbycode = IntegerField(db_column='mWeighedbyCode', null=True)
    mweighedbyname = TextField(db_column='mWeighedbyName', null=True)  # varchar
    mweighedtime = DateTimeField(db_column='mWeighedtime', null=True)

    class Meta:
        db_table = 'Paste Errors'
        primary_key = False

class Purchasedtl(BaseModel):
    ddate = DateTimeField(db_column='dDate', null=True)
    dleafcode = IntegerField(db_column='dLeafcode', null=True)
    dnettweight = IntegerField(db_column='dNettweight', null=True)
    dsuppcode = IntegerField(db_column='dSuppcode', null=True)

    class Meta:
        db_table = 'PurchaseDtl'
        primary_key = False

class Roundoff(BaseModel):
    mroundoff = FloatField(db_column='mRoundoff', null=True)

    class Meta:
        db_table = 'Roundoff'
        primary_key = False

class Sheddeductiondetails(BaseModel):
    mdeductweight = IntegerField(db_column='mDeductWeight', null=True)
    mdeductiontype = TextField(db_column='mDeductionType', null=True)  # varchar
    mdeductioncode = IntegerField(db_column='mDeductioncode', null=True)
    mshedsupplyhdrcode = IntegerField(db_column='mShedSupplyHdrCode', null=True)

    class Meta:
        db_table = 'ShedDeductionDetails'
        primary_key = False

class Shedleafsupplyhdr(BaseModel):
    ma = IntegerField(db_column='mA', null=True)
    mb = IntegerField(db_column='mB', null=True)
    mbb = IntegerField(db_column='mBB', null=True)
    mc = IntegerField(db_column='mC', null=True)
    mcheckedbycode = IntegerField(db_column='mCheckedbyCode', null=True)
    mcheckedbyname = TextField(db_column='mCheckedbyName', null=True)  # varchar
    mcomcode = IntegerField(db_column='mComCode', null=True)
    mconfirmation = IntegerField(db_column='mConfirmation', null=True)
    mdeductionweight = IntegerField(db_column='mDeductionweight', null=True)
    mexcessweight = IntegerField(db_column='mExcessweight', null=True)
    mgrossweight = IntegerField(db_column='mGrossweight', null=True)
    mmode = TextField(db_column='mMode', null=True)  # varchar
    mnetweight = IntegerField(db_column='mNetweight', null=True)
    mrecdbags = IntegerField(db_column='mRecdBags', null=True)
    mshedcode = IntegerField(db_column='mShedCode', null=True)
    mshedname = TextField(db_column='mShedName', null=True)  # varchar
    mshortageweight = IntegerField(db_column='mShortageWeight', null=True)
    msupplycode = IntegerField(db_column='mSupplyCode', null=True)
    msupplydate = DateTimeField(db_column='mSupplydate', null=True)
    mtransferweight = IntegerField(db_column='mTransferweight', null=True)
    mtrsfbags = IntegerField(db_column='mTrsfBags', null=True)
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)
    mvehiclein = DateTimeField(db_column='mVehicleIn', null=True)
    mvehiclename = TextField(db_column='mVehicleName', null=True)  # varchar
    mvehicleout = DateTimeField(db_column='mVehicleOut', null=True)
    mweighedbycode = IntegerField(db_column='mWeighedbyCode', null=True)
    mweighedbyname = TextField(db_column='mWeighedbyName', null=True)  # varchar
    mconfirmedtime = DateTimeField(null=True)
    mweighedtime = DateTimeField(null=True)

    class Meta:
        db_table = 'ShedLeafSupplyHdr'
        primary_key = False

class Shedmst(BaseModel):
    mshedcode = IntegerField(db_column='mShedCode', null=True)
    mshedname = TextField(db_column='mShedName', null=True)  # varchar

    class Meta:
        db_table = 'ShedMst'
        primary_key = False

class Shedleafsupplyinbag(BaseModel):
    mbagweight = FloatField(db_column='mBagWeight', null=True)
    mnoofbags = IntegerField(db_column='mNoofBags', null=True)
    mshedsupplyhdrcode = IntegerField(db_column='mShedSupplyHdrCode', null=True)

    class Meta:
        db_table = 'ShedleafSupplyinbag'
        primary_key = False

class Staffmst(BaseModel):
    mstaffname = TextField(db_column='mStaffName', null=True)  # varchar
    mstaffpassword = TextField(db_column='mStaffPassword', null=True)  # varchar
    mstaffcode = IntegerField(db_column='mStaffcode', null=True)

    class Meta:
        db_table = 'StaffMst'
        primary_key = False

class Suppliermst(BaseModel):
    mmobileno = TextField(db_column='mMobileNo', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    msupplierfathername = TextField(db_column='mSupplierFatherName', null=True)  # varchar
    msuppliername = TextField(db_column='mSupplierName', null=True)  # varchar
    msuppliershedcode = IntegerField(db_column='mSupplierShedCode', null=True)
    msuppliershedname = TextField(db_column='mSupplierShedName', null=True)  # varchar
    msuppliershedtype = IntegerField(db_column='mSupplierShedType', null=True)
    msuppliervillage = TextField(db_column='mSupplierVillage', null=True)  # varchar

    class Meta:
        db_table = 'SupplierMst'
        primary_key = False

class Suppliermstold(BaseModel):
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    msupplierfathername = TextField(db_column='mSupplierFatherName', null=True)  # varchar
    msuppliername = TextField(db_column='mSupplierName', null=True)  # varchar
    msuppliershedcode = IntegerField(db_column='mSupplierShedCode', null=True)
    msuppliershedname = TextField(db_column='mSupplierShedName', null=True)  # varchar
    msuppliershedtype = IntegerField(db_column='mSupplierShedType', null=True)
    msuppliervillage = TextField(db_column='mSupplierVillage', null=True)  # varchar

    class Meta:
        db_table = 'SupplierMstold'
        primary_key = False

class Temp(BaseModel):
    mdate = DateTimeField(db_column='mDate', null=True)
    mkgs = IntegerField(db_column='mKgs', null=True)
    msuppliername = TextField(db_column='mSuppliername', null=True)  # varchar
    mtype = TextField(db_column='mType', null=True)  # varchar

    class Meta:
        db_table = 'Temp'
        primary_key = False

class Tempstore(BaseModel):
    mbagserialno = IntegerField(db_column='mBagSerialNo', null=True)
    mbagweight = IntegerField(db_column='mBagWeight', null=True)
    mbagno = IntegerField(db_column='mBagno', null=True)
    mbags = IntegerField(db_column='mBags', null=True)
    mcode = IntegerField(db_column='mCode', null=True)
    mdate = DateTimeField(db_column='mDate', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    mtime = DateTimeField(db_column='mTime', null=True)
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)

    class Meta:
        db_table = 'TempStore'
        primary_key = False

class Tempstore1(BaseModel):
    mbagserialno = IntegerField(db_column='mBagSerialNo', null=True)
    mbagweight = IntegerField(db_column='mBagWeight', null=True)
    mbagno = IntegerField(db_column='mBagno', null=True)
    mbags = IntegerField(db_column='mBags', null=True)
    mcode = IntegerField(db_column='mCode', null=True)
    mdate = DateTimeField(db_column='mDate', null=True)
    msuppliercode = IntegerField(db_column='mSupplierCode', null=True)
    mtime = DateTimeField(db_column='mTime', null=True)
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)

    class Meta:
        db_table = 'TempStore1'
        primary_key = False

class Troughdetails(BaseModel):
    mdate = DateTimeField(db_column='mDate', null=True)
    msupplyhdrcode = IntegerField(db_column='mSupplyHdrCode', null=True)
    mtroughname = TextField(db_column='mTroughName', null=True)  # varchar
    mweight = FloatField(db_column='mWeight', null=True)

    class Meta:
        db_table = 'TroughDetails'
        primary_key = False

class Turfmst(BaseModel):
    mturfname = TextField(db_column='mTurfName', null=True)  # varchar

    class Meta:
        db_table = 'TurfMst'
        primary_key = False

class Vehiclemst(BaseModel):
    mvehiclecode = IntegerField(db_column='mVehicleCode', null=True)
    mvehiclename = TextField(db_column='mVehicleName', null=True)  # varchar

    class Meta:
        db_table = 'VehicleMst'
        primary_key = False

class W(BaseModel):
    mdate = DateTimeField(db_column='mDate', null=True)
    mmodweight = TextField(db_column='mModWeight', null=True)  # varchar
    mtime = DateTimeField(db_column='mTime', null=True)
    mweight = TextField(db_column='mWeight', null=True)  # varchar

    class Meta:
        db_table = 'W'
        primary_key = False

class Wconfig(BaseModel):
    mbitspersecond = IntegerField(db_column='mBitsPerSecond', null=True)
    mdatabits = IntegerField(db_column='mDataBits', null=True)
    mfirst = IntegerField(db_column='mFirst', null=True)
    mparity = TextField(db_column='mParity', null=True)  # varchar
    mport = IntegerField(db_column='mPort', null=True)
    msecond = IntegerField(db_column='mSecond', null=True)
    mstopbits = IntegerField(db_column='mStopBits', null=True)

    class Meta:
        db_table = 'WConfig'
        primary_key = False

