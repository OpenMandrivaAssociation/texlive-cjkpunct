Name:		texlive-cjkpunct
Version:	4.8.1.2
Release:	1
Summary:	Adjust locations and kerning of CJK punctuation marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/chinese/cjkpunct
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package serves as a companion package for CJK.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
