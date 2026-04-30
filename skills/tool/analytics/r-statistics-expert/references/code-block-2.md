# r Example

```
library(ggplot2)
library(viridis)
library(patchwork)

# Distribution plot
ggplot(df_clean, aes(x = score, fill = treatment)) +
  geom_density(alpha = 0.6) +
  geom_vline(aes(xintercept = mean(score)), linetype = "dashed") +
  scale_fill_viridis(discrete = TRUE) +
  labs(title = "Score Distribution by Treatment",
       x = "Score", y = "Density", fill = "Treatment") +
  theme_minimal(base_size = 12)

# Boxplot with jitter
ggplot(df_clean, aes(x = treatment, y = score, color = gender)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter(alpha = 0.3, width = 0.2) +
  stat_summary(fun = "mean", geom = "point", size = 3, shape = 4) +
  facet_wrap(~bmi_category, scales = "free_y") +
  theme_classic()

# Time series
df_clean |>
  group_by(date, treatment) |>
  summarise(daily_mean = mean(score, na.rm = TRUE), .groups = "drop") |>
  ggplot(aes(x = date, y = daily_mean, color = treatment)) +
  geom_line() +
  geom_ribbon(aes(ymin = daily_mean - sd(score), ymax = daily_mean + sd(score),
                  fill = treatment), alpha = 0.2, linetype = 0) +
  scale_color_brewer(palette = "Set1") +
  labs(title = "Score Over Time", x = "Date", y = "Mean Score") +
  theme_minimal()
```
