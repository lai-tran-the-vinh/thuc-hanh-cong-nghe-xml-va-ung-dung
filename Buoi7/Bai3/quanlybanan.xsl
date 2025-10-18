<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:strip-space elements="*"/>
  
  <xsl:key name="nvByID" match="NHANVIEN" use="MANV"/>
  <xsl:key name="monByID" match="MON" use="MAMON"/>
  <xsl:key name="banByID" match="BAN" use="SOBAN"/>
  
  <xsl:key name="hdByNV" match="HOADON" use="MANV"/>
  <xsl:key name="hdByBan" match="HOADON" use="SOBAN"/>
  <xsl:key name="cthdByMon" match="CTHD" use="MAMON"/>
  
  
  <xsl:template match="/">
    <html>
      <head>
        <title>Quản lý bàn ăn</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 25px; background-color: #fcfcfc; }
          h1 { color: #2a5d84; }
          h3 { color: #005a9c; border-bottom: 2px solid #005a9c; padding-bottom: 5px; margin-top: 30px;}
          table { 
          border-collapse: collapse; 
          width: 90%; 
          margin-bottom: 20px; 
          box-shadow: 0 1px 3px rgba(0,0,0,0.1);
          }
          th, td { 
          border: 1px solid #ddd; 
          padding: 10px; 
          text-align: left; 
          }
          th { 
          background-color: #007bff; 
          color: white; 
          font-weight: bold;
          }
          tr:nth-child(even) { background-color: #f8f9fa; }
          tr:hover { background-color: #e9ecef; }
        </style>
      </head>
      <body>
        <h1>Quản lý bàn ăn</h1>
        <xsl:apply-templates select="QUANLY"/>
      </body>
    </html>
  </xsl:template>
  
  <xsl:template match="QUANLY">
    
    <h3>1. Danh sách tất cả các bàn</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Số Bàn</th>
          <th>Tên Bàn</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="BANS/BAN" mode="q1"/>
      </tbody>
    </table>
    
    <h3>2. Danh sách nhân viên</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Mã NV</th>
          <th>Tên NV</th>
          <th>SĐT</th>
          <th>Địa chỉ</th>
          <th>Giới tính</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="NHANVIENS/NHANVIEN" mode="q2"/>
      </tbody>
    </table>
    
    <h3>3. Danh sách món ăn</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Mã Món</th>
          <th>Tên Món</th>
          <th>Giá</th>
          <th>Hình Ảnh</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="MONS/MON" mode="q3"/>
      </tbody>
    </table>
    
    <h3>4. Thông tin của nhân viên NV02</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Mã NV</th>
          <th>Tên NV</th>
          <th>SĐT</th>
          <th>Địa chỉ</th>
          <th>Giới tính</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="NHANVIENS/NHANVIEN[MANV='NV02']" mode="q2"/>
      </tbody>
    </table>
    
    <h3>5. Danh sách món ăn có giá trên 50,000</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Mã Món</th>
          <th>Tên Món</th>
          <th>Giá</th>
          <th>Hình Ảnh</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="MONS/MON[GIA > 50000]" mode="q3"/>
      </tbody>
    </table>
    
    <h3>6. Thông tin hóa đơn HD03 (Tên NV, Bàn, Ngày lập, Tổng tiền)</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên NV Phục Vụ</th>
          <th>Số Bàn</th>
          <th>Ngày Lập</th>
          <th>Tổng Tiền</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="HOADONS/HOADON[SOHD='HD03']" mode="q6"/>
      </tbody>
    </table>
    
    <h3>7. Tên các món ăn trong hóa đơn HD02</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên Món Ăn</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="HOADONS/HOADON[SOHD='HD02']/CTHDS/CTHD" mode="q7"/>
      </tbody>
    </table>
    
    <h3>8. Tên nhân viên lập hóa đơn HD02</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên Nhân Viên</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="HOADONS/HOADON[SOHD='HD02']" mode="q8"/>
      </tbody>
    </table>
    
    <h3>9. Đếm số bàn</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Nội dung</th>
          <th>Số lượng</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="BANS" mode="q9"/>
      </tbody>
    </table>
    
    <h3>10. Đếm số hóa đơn lập bởi NV01</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Nội dung</th>
          <th>Số lượng</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="NHANVIENS/NHANVIEN[MANV='NV01']" mode="q10"/>
      </tbody>
    </table>
    
    <h3>11. Danh sách các món (không trùng lặp) đã bán cho bàn số 2</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên Món Ăn</th>
        </tr>
      </thead>
      <tbody>
        <xsl:variable name="all_mons_for_ban2" select="key('monByID', key('hdByBan', '2')/CTHDS/CTHD/MAMON)"/>
        <xsl:apply-templates select="$all_mons_for_ban2[generate-id() = generate-id(key('monByID', MAMON)[1])]" mode="q11"/>
      </tbody>
    </table>
    
    <h3>12. Danh sách nhân viên (không trùng lặp) đã lập HĐ cho bàn số 3</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên Nhân Viên</th>
        </tr>
      </thead>
      <tbody>
        <xsl:variable name="all_nv_for_ban3" select="key('nvByID', key('hdByBan', '3')/MANV)"/>
        <xsl:apply-templates select="$all_nv_for_ban3[generate-id() = generate-id(key('nvByID', MANV)[1])]" mode="q12"/>
      </tbody>
    </table>
    
    <h3>13. Các món ăn được bán với tổng số lượng > 1</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Tên Món Ăn</th>
          <th>Tổng Số Lượng Đã Bán</th>
        </tr>
      </thead>
      <tbody>
        <xsl:variable name="all_sold_mons" select="key('monByID', //CTHD/MAMON)"/>
        <xsl:variable name="distinct_sold_mons" select="$all_sold_mons[generate-id() = generate-id(key('monByID', MAMON)[1])]"/>
        <xsl:apply-templates select="$distinct_sold_mons" mode="q13"/>
      </tbody>
    </table>
    
    <h3>14. Chi tiết hóa đơn HD04</h3>
    <table>
      <thead>
        <tr>
          <th>STT</th>
          <th>Mã Món</th>
          <th>Tên Món</th>
          <th>Đơn Giá</th>
          <th>Số Lượng</th>
          <th>Thành Tiền</th>
        </tr>
      </thead>
      <tbody>
        <xsl:apply-templates select="HOADONS/HOADON[SOHD='HD04']/CTHDS/CTHD" mode="q14"/>
      </tbody>
    </table>
    
  </xsl:template>
  
  
  <xsl:template match="BAN" mode="q1">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="SOBAN"/></td>
      <td><xsl:value-of select="TENBAN"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="NHANVIEN" mode="q2">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="MANV"/></td>
      <td><xsl:value-of select="TENV"/></td>
      <td><xsl:value-of select="SDT"/></td>
      <td><xsl:value-of select="DIACHI"/></td>
      <td><xsl:value-of select="GIOITINH"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="MON" mode="q3">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="MAMON"/></td>
      <td><xsl:value-of select="TENMON"/></td>
      <td><xsl:value-of select="GIA"/></td>
      <td><xsl:value-of select="HINHANH"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="HOADON" mode="q6">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="key('nvByID', MANV)/TENV"/></td>
      <td><xsl:value-of select="SOBAN"/></td>
      <td><xsl:value-of select="NGAYLAP"/></td>
      <td><xsl:value-of select="TONGTIEN"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="CTHD" mode="q7">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="key('monByID', MAMON)/TENMON"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="HOADON" mode="q8">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="key('nvByID', MANV)/TENV"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="BANS" mode="q9">
    <tr>
      <td>1</td>
      <td>Tổng số bàn</td>
      <td><xsl:value-of select="count(BAN)"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="NHANVIEN" mode="q10">
    <tr>
      <td>1</td>
      <td>Số hóa đơn lập bởi <xsl:value-of select="TENV"/> (NV01)</td>
      <td><xsl:value-of select="count(key('hdByNV', MANV))"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="MON" mode="q11">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="TENMON"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="NHANVIEN" mode="q12">
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="TENV"/></td>
    </tr>
  </xsl:template>
  
  <xsl:template match="MON" mode="q13">
    <xsl:variable name="tong_so_luong" select="sum(key('cthdByMon', MAMON)/SOLUONG)"/>
    
    <xsl:if test="$tong_so_luong > 1">
      <tr>
        <td><xsl:number/></td>
        <td><xsl:value-of select="TENMON"/></td>
        <td><xsl:value-of select="$tong_so_luong"/></td>
      </tr>
    </xsl:if>
  </xsl:template>
  
  <xsl:template match="CTHD" mode="q14">
    <xsl:variable name="mon_hien_tai" select="key('monByID', MAMON)"/>
    
    <xsl:variable name="so_luong" select="SOLUONG"/>
    <xsl:variable name="don_gia" select="$mon_hien_tai/GIA"/>
    <xsl:variable name="thanh_tien" select="$so_luong * $don_gia"/>
    
    <tr>
      <td><xsl:number/></td>
      <td><xsl:value-of select="MAMON"/></td>
      <td><xsl:value-of select="$mon_hien_tai/TENMON"/></td>
      <td><xsl:value-of select="$don_gia"/></td>
      <td><xsl:value-of select="$so_luong"/></td>
      <td><xsl:value-of select="$thanh_tien"/></td>
    </tr>
  </xsl:template>
  
</xsl:stylesheet>