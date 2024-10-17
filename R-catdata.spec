%global packname  catdata
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1
Release:          1
Summary:          Categorical Data
Group:            Sciences/Mathematics
License:          GPLv2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

Requires:         R-MASS 

Requires:         R-rms R-qvcalc R-glmmML R-nnet R-pscl R-VGAM R-gee R-mlogit R-Ecdat R-geepack R-mgcv R-rpart R-party R-ordinal R-lme4 R-vcdExtra R-glmnet R-mboost R-class R-e1071 R-flexmix R-lqa R-lpSolve R-GAMBoost R-penalized 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-MASS

BuildRequires:   R-rms R-qvcalc R-glmmML R-nnet R-pscl R-VGAM R-gee R-mlogit R-Ecdat R-geepack R-mgcv R-rpart R-party R-ordinal R-lme4 R-vcdExtra R-glmnet R-mboost R-class R-e1071 R-flexmix R-lqa R-lpSolve R-GAMBoost R-penalized 
%description
This R-package contains examples from the book "Regression for Categorical
Data", Tutz 2011, Cambridge University Press. The names of the examples
refer to the chapter and the data set that is used.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
