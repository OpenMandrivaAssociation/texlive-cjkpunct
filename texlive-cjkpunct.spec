%global tl_name cjkpunct
%global tl_revision 41119

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.8.4
Release:	%{tl_revision}.1
Summary:	Adjust locations and kerning of CJK punctuation marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/chinese/cjkpunct
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cjkpunct.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package serves as a companion package for CJK.

