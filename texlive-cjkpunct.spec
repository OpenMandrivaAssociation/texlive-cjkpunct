# revision 15878
# category Package
# catalog-ctan /language/chinese/cjkpunct
# catalog-date 2009-11-09 14:16:05 +0100
# catalog-license lppl
# catalog-version 4.8.1-2
Name:		texlive-cjkpunct
Version:	4.8.1.2
Release:	9
Summary:	Adjust locations and kerning of CJK punctuation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/chinese/cjkpunct
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package serves as a companion package for CJK.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cjkpunct/CJKpunct.sty
%doc %{_texmfdistdir}/doc/latex/cjkpunct/CJKpunct.pdf
%doc %{_texmfdistdir}/doc/latex/cjkpunct/CJKpunct.spa
%doc %{_texmfdistdir}/doc/latex/cjkpunct/README
%doc %{_texmfdistdir}/doc/latex/cjkpunct/README.zh-cn.txt
%doc %{_texmfdistdir}/doc/latex/cjkpunct/examples/example-CJKfntef.tex
%doc %{_texmfdistdir}/doc/latex/cjkpunct/examples/example-gb.tex
%doc %{_texmfdistdir}/doc/latex/cjkpunct/examples/example-gbk.tex
%doc %{_texmfdistdir}/doc/latex/cjkpunct/examples/example-utf8.tex
%doc %{_texmfdistdir}/doc/latex/cjkpunct/setpunct/setpunct-macros.tex
%doc %{_texmfdistdir}/doc/latex/cjkpunct/setpunct/setpunct-main.tex
#- source
%doc %{_texmfdistdir}/source/latex/cjkpunct/CJKpunct.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.8.1.2-2
+ Revision: 750249
- Rebuild to reduce used resources

* Sun Nov 06 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.8.1.2-1
+ Revision: 722997
- texlive-cjkpunct
- texlive-cjkpunct
- texlive-cjkpunct
- texlive-cjkpunct
- texlive-cjkpunct
- texlive-cjkpunct

