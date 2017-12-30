Name:		texlive-cjkpunct
Version:	4.8.4
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
%{_texmfdistdir}/tex/latex/cjkpunct
%doc %{_texmfdistdir}/doc/latex/cjkpunct
#- source
%doc %{_texmfdistdir}/source/latex/cjkpunct

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
