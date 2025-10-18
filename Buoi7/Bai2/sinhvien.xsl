<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" encoding="UTF-8" indent="no" />
    <xsl:strip-space elements="*" />

    <xsl:template match="school">
        <xsl:text>[</xsl:text>

        <xsl:apply-templates select="student" />

        <xsl:text>]</xsl:text>
    </xsl:template>

    <xsl:template match="student">
        <xsl:text>{</xsl:text>

        <xsl:text>"ma": "</xsl:text>
        <xsl:value-of select="id" />
        <xsl:text>", </xsl:text>

        <xsl:text>"hoTen": "</xsl:text>
        <xsl:value-of select="name" />
        <xsl:text>", </xsl:text>

        <xsl:text>"ngaySinh": "</xsl:text>
        <xsl:value-of select="date" />
        <xsl:text>"</xsl:text>

        <xsl:text>}</xsl:text>

        <xsl:if test="position() != last()">
            <xsl:text>,</xsl:text>
        </xsl:if>
    </xsl:template>

</xsl:stylesheet>