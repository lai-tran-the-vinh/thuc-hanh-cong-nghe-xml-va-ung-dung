<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" encoding="UTF-8" indent="yes" />

    <xsl:key name="studentByID" match="student" use="id" />

    <xsl:key name="enrollmentByCourseID" match="enrollment" use="courseRef" />

    <xsl:key name="enrollmentByStudentID" match="enrollment" use="studentRef" />


    <xsl:template match="/">
        <html>
            <head>
                <title>Kết quả Truy vấn Sinh viên</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9;
                    }
                    h1 { color: #004a99; }
                    h3 { color: #0066cc; border-bottom: 2px solid #0066cc; padding-bottom: 5px; }
                    table {
                    border-collapse: collapse;
                    width: 70%;
                    margin-bottom: 30px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                    th, td {
                    border: 1px solid #ddd;
                    padding: 10px;
                    text-align: left;
                    }
                    th {
                    background-color: #007bff;
                    color: white;
                    }
                    tr:nth-child(even) { background-color: #f2f2f2; }
                    tr:hover { background-color: #e6f7ff; }
                </style>
            </head>
            <body>
                <h1>Báo cáo Thông tin Trường học</h1>
                <xsl:apply-templates select="school" />
            </body>
        </html>
    </xsl:template>

    <xsl:template match="school">

        <h3>1. Liệt kê thông tin của tất cả sinh viên</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã SV</th>
                    <th>Họ Tên</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="student" mode="query1" />
            </tbody>
        </table>

        <h3>2. Danh sách sinh viên theo điểm (cao đến thấp)</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã SV</th>
                    <th>Họ Tên</th>
                    <th>Điểm</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="student" mode="query2">
                    <xsl:sort select="grade" data-type="number" order="descending" />
                </xsl:apply-templates>
            </tbody>
        </table>

        <h3>3. Danh sách sinh viên (sắp xếp theo tháng sinh)</h3>
        <table>
            <thead>
                <tr>
                    <th>STT</th>
                    <th>Họ Tên</th>
                    <th>Ngày Sinh</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="student" mode="query3">
                    <xsl:sort select="substring(date, 6, 2)" data-type="number" order="ascending" />
                    <xsl:sort select="substring(date, 9, 2)" data-type="number" order="ascending" />
                </xsl:apply-templates>
            </tbody>
        </table>

        <h3>4. Danh sách các khóa học có sinh viên đăng ký</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã Khóa Học</th>
                    <th>Tên Khóa Học</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="course[key('enrollmentByCourseID', id)]" mode="query4">
                    <xsl:sort select="name" order="ascending" />
                </xsl:apply-templates>
            </tbody>
        </table>

        <h3>5. Danh sách sinh viên đăng ký khóa học "Hóa học 201"</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã SV</th>
                    <th>Họ Tên</th>
                </tr>
            </thead>
            <tbody>
                <xsl:variable name="courseID_HoaHoc" select="course[name='Hóa học 201']/id" />

                <xsl:variable name="studentRefs_HocHoa"
                    select="key('enrollmentByCourseID', $courseID_HoaHoc)/studentRef" />

                <xsl:apply-templates select="key('studentByID', $studentRefs_HocHoa)" mode="query1" />
            </tbody>
        </table>

        <h3>6. Danh sách sinh viên sinh năm 1997</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã SV</th>
                    <th>Họ Tên</th>
                    <th>Ngày Sinh</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="student[substring(date, 1, 4) = '1997']" mode="query6" />
            </tbody>
        </table>

        <h3>7. Danh sách sinh viên họ “Trần”</h3>
        <table>
            <thead>
                <tr>
                    <th>Mã SV</th>
                    <th>Họ Tên</th>
                </tr>
            </thead>
            <tbody>
                <xsl:apply-templates select="student[starts-with(name, 'Trần')]" mode="query1" />
            </tbody>
        </table>

    </xsl:template>


    <xsl:template match="student" mode="query1">
        <tr>
            <td>
                <xsl:value-of select="id" />
            </td>
            <td>
                <xsl:value-of select="name" />
            </td>
        </tr>
    </xsl:template>

    <xsl:template match="student" mode="query2">
        <tr>
            <td>
                <xsl:value-of select="id" />
            </td>
            <td>
                <xsl:value-of select="name" />
            </td>
            <td>
                <xsl:value-of select="grade" />
            </td>
        </tr>
    </xsl:template>

    <xsl:template match="student" mode="query3">
        <tr>
            <td>
                <xsl:number />
            </td>
            <td>
                <xsl:value-of select="name" />
            </td>
            <td>
                <xsl:value-of select="date" />
            </td>
        </tr>
    </xsl:template>

    <xsl:template match="course" mode="query4">
        <tr>
            <td>
                <xsl:value-of select="id" />
            </td>
            <td>
                <xsl:value-of select="name" />
            </td>
        </tr>
    </xsl:template>

    <xsl:template match="student" mode="query6">
        <tr>
            <td>
                <xsl:value-of select="id" />
            </td>
            <td>
                <xsl:value-of select="name" />
            </td>
            <td>
                <xsl:value-of select="date" />
            </td>
        </tr>
    </xsl:template>

</xsl:stylesheet>