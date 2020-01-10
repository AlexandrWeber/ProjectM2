<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>
<xsl:template match="/">
<html>
<head>
<title>
<xsl:value-of select="Page/Info/Titre"/>
-
<xsl:value-of select="Page/Info/Auteurs"/>
- 
<xsl:value-of select="Page/Info/Date"/>
</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<link href="design.css" rel="stylesheet"/>
</head>
<body>
<div id="banner">
<h1>
<xsl:value-of select="Page/Info/Titre"/>
</h1>
<h3>
<xsl:value-of select="Page/Info/Auteurs"/>
</h3>
<h3>
<xsl:value-of select="Page/Info/Date"/>
</h3>
</div>
<hr/>
<div id="menu">
<ul>
<xsl:for-each select="Page/Menu/Rubrique">
<li>
<a>
<xsl:attribute name="href">
<xsl:value-of select="./@lien"/>
</xsl:attribute>
<xsl:value-of select="."/>
</a>
</li>
</xsl:for-each>
</ul>
</div>
<div id="content">
<xsl:apply-templates select="Page/Contenu"/>
</div>
<hr/>
</body>
</html>
</xsl:template>
<xsl:template match="Page/Contenu/Titre">
<h1>
<xsl:value-of select="."/>
</h1>
</xsl:template>
<xsl:template match="Page/Contenu/Soustitre">
<h2>
<xsl:value-of select="."/>
</h2>
</xsl:template>
<xsl:template match="Page/Contenu/Soustitre1">
<h3>
<xsl:value-of select="."/>
</h3>
</xsl:template>
<xsl:template match="Page/Contenu/Paragraphe">
<p>
<xsl:value-of select="."/>
</p>
</xsl:template>
<xsl:template match="//Contenu/Enonce">
<div class="blueBox">
<e>
<xsl:for-each select="Texte">
<texte>
<xsl:value-of select="."/>
<br/>
</texte>
</xsl:for-each>
<xsl:for-each select="Illustration">
<texte>
<i>
<xsl:value-of select="."/>
</i>
</texte>
</xsl:for-each>
<xsl:for-each select="Liste">
<ul class="a">
<li>
<xsl:value-of select="."/>
</li>
</ul>
</xsl:for-each>
<xsl:for-each select="SousListe">
<ul>
<li>
<xsl:value-of select="."/>
</li>
</ul>
</xsl:for-each>
</e>
</div>
<br/>
</xsl:template>
<xsl:template match="//Contenu/Liste">
<xsl:for-each select="Liste">
<ul class="a">
<li>
<xsl:value-of select="."/>
</li>
</ul>
</xsl:for-each>
<xsl:for-each select="SousListe">
<ul>
<li>
<xsl:value-of select="."/>
</li>
</ul>
</xsl:for-each>
</xsl:template>
<xsl:template match="Page/Contenu/Resultat">
<pe>
<xsl:value-of select="."/>
</pe>
</xsl:template>
<xsl:template match="Page/Contenu/Fichiers">
<xsl:for-each select="Fichier[.!='']">
<a href="{./@lien}" target="_blank">
<xsl:value-of select="."/>
<xsl:if test="position()!=last()">, </xsl:if>
</a>
</xsl:for-each>
</xsl:template>
<xsl:template match="Page/Contenu/NosFichiers">
<xsl:for-each select="Fichier[.!='']">
<a href="{./@lien}" target="_blank">
• 
<xsl:value-of select="."/>
</a>
<br/>
</xsl:for-each>
</xsl:template>
<xsl:template match="Page/Contenu/Illustration">
<pi>
<xsl:value-of select="."/>
</pi>
</xsl:template>
<xsl:template match="Page/Contenu/ImageIdx">
<div class="center">
<img>
<xsl:attribute name="src">
<xsl:value-of select="."/>
</xsl:attribute>
<xsl:attribute name="width">65%</xsl:attribute>
<xsl:attribute name="border">2</xsl:attribute>
					<xsl:attribute name="height">90%</xsl:attribute>
</img>
</div>
<br/>
</xsl:template>
</xsl:stylesheet>
