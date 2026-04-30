# r Example

```
library(broom)
library(lme4)
library(survival)

# Linear regression
fit_lm <- lm(score ~ age + gender + treatment, data = df_clean)
tidy(fit_lm, conf.int = TRUE, conf.level = 0.95)
glance(fit_lm)  # R², AIC, residual diagnostics

# Logistic regression
fit_glm <- glm(outcome ~ age + bmi_category + treatment,
               data = df_clean, family = binomial())
tidy(fit_glm, exponentiate = TRUE, conf.int = TRUE)
# Odds ratios: exp(estimate) = odds ratio

# Mixed-effects model (repeated measures)
fit_lmer <- lmer(score ~ treatment + (1|subject_id) + (1|site),
                 data = df_clean)
tidy(fit_lmer, effects = "fixed")
tidy(fit_lmer, effects = "ran_pars")

# Survival analysis
fit_surv <- survfit(Surv(time, event) ~ treatment, data = df_clean)
ggsurvplot(fit_surv, data = df_clean, conf.int = TRUE)
coxph(Surv(time, event) ~ treatment + age, data = df_clean) |>
  tidy(exponentiate = TRUE)

# ANOVA
fit_aov <- aov(score ~ treatment * gender + Error(subject), data = df_clean)
summary(fit_aov)
```
