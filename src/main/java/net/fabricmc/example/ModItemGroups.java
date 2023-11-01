package net.fabricmc.example;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.block.Blocks;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registry;
import net.minecraft.registry.Registries;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

public class ModItemGroups {

    public static final RegistryKey<ItemGroup> TERRACOTTA_GROUP = RegistryKey.of(RegistryKeys.ITEM_GROUP, new Identifier("moreterracotta", "terracotta_group"));
    public static final RegistryKey<ItemGroup> CONCRETE_GROUP = RegistryKey.of(RegistryKeys.ITEM_GROUP, new Identifier("moreterracotta", "concrete_group"));

    public static void initialiseItemGroups() {
        Registry.register(Registries.ITEM_GROUP, TERRACOTTA_GROUP, FabricItemGroup.builder()
                .displayName(Text.translatable("More Terracotta"))
                .icon(() -> new ItemStack(Blocks.TERRACOTTA))
                .build());

        Registry.register(Registries.ITEM_GROUP, CONCRETE_GROUP,  FabricItemGroup.builder()
                .displayName(Text.translatable("More Concrete"))
                .icon(() -> new ItemStack(Blocks.WHITE_CONCRETE))
                .build());
    }


}
